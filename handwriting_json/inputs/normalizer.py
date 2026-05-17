"""Normalize user-provided document inputs."""

from __future__ import annotations

import base64
import binascii
import mimetypes
from pathlib import Path
from typing import BinaryIO
from urllib.parse import urlparse

import httpx

from handwriting_json.errors import InputError
from handwriting_json.models import DocumentInput

SUPPORTED_MEDIA_TYPES = {
    "application/pdf",
    "image/png",
    "image/jpeg",
    "image/webp",
}


def normalize_input(source: str | Path | bytes | BinaryIO, *, document_id: str | None = None) -> DocumentInput:
    """Normalize a local path, URL, base64 string, bytes, or file-like object."""
    if isinstance(source, Path):
        return _from_path(source, document_id=document_id)

    if isinstance(source, bytes):
        return _from_bytes(source, document_id=document_id or "document", source_label="bytes")

    if hasattr(source, "read"):
        return _from_file_object(source, document_id=document_id)

    if isinstance(source, str):
        stripped = source.strip()
        if _looks_like_url(stripped):
            return _from_url(stripped, document_id=document_id)

        path = Path(stripped).expanduser()
        if path.exists():
            return _from_path(path, document_id=document_id)

        return _from_base64(stripped, document_id=document_id)

    raise InputError(f"Unsupported input type: {type(source).__name__}")


def _from_path(path: Path, *, document_id: str | None) -> DocumentInput:
    if not path.is_file():
        raise InputError(f"Input path is not a file: {path}")

    media_type = _detect_media_type(path.name, path.read_bytes())
    _validate_media_type(media_type)
    return DocumentInput(
        document_id=document_id or path.name,
        media_type=media_type,
        data=path.read_bytes(),
        source=str(path),
    )


def _from_url(url: str, *, document_id: str | None) -> DocumentInput:
    try:
        response = httpx.get(url, timeout=30.0)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        raise InputError(f"Could not fetch input URL: {exc}") from exc

    name = Path(urlparse(url).path).name or "document"
    media_type = response.headers.get("content-type", "").split(";")[0].strip()
    if not media_type:
        media_type = _detect_media_type(name, response.content)
    _validate_media_type(media_type)

    return DocumentInput(
        document_id=document_id or name,
        media_type=media_type,
        data=response.content,
        source=url,
        metadata={"url": url},
    )


def _from_base64(value: str, *, document_id: str | None) -> DocumentInput:
    if "," in value and value.lower().startswith("data:"):
        header, encoded = value.split(",", 1)
        media_type = header.removeprefix("data:").split(";")[0]
    else:
        encoded = value
        media_type = ""

    try:
        data = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise InputError("Input is not an existing path, URL, or valid base64 document") from exc

    media_type = media_type or _detect_media_type(document_id or "document", data)
    _validate_media_type(media_type)
    return DocumentInput(
        document_id=document_id or "document",
        media_type=media_type,
        data=data,
        source="base64",
    )


def _from_bytes(data: bytes, *, document_id: str, source_label: str) -> DocumentInput:
    media_type = _detect_media_type(document_id, data)
    _validate_media_type(media_type)
    return DocumentInput(document_id=document_id, media_type=media_type, data=data, source=source_label)


def _from_file_object(file_obj: BinaryIO, *, document_id: str | None) -> DocumentInput:
    name = Path(getattr(file_obj, "name", "")).name or document_id or "document"
    data = file_obj.read()
    if isinstance(data, str):
        data = data.encode("utf-8")
    return _from_bytes(data, document_id=document_id or name, source_label=name)


def _detect_media_type(name: str, data: bytes) -> str:
    if data.startswith(b"%PDF"):
        return "application/pdf"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "image/webp"

    guessed, _ = mimetypes.guess_type(name)
    return guessed or "application/octet-stream"


def _validate_media_type(media_type: str) -> None:
    if media_type not in SUPPORTED_MEDIA_TYPES:
        supported = ", ".join(sorted(SUPPORTED_MEDIA_TYPES))
        raise InputError(f"Unsupported media type '{media_type}'. Supported types: {supported}")


def _looks_like_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
