"""Public extraction API."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

from handwriting_json.errors import ResponseParseError
from handwriting_json.inputs import normalize_input
from handwriting_json.models import ExtractionResult
from handwriting_json.prompts import build_extraction_prompt
from handwriting_json.providers import LiteLLMProvider, Provider
from handwriting_json.schemas import load_schema_guidance


def extract(
    source: str | Path | bytes | Any,
    *,
    model: str,
    provider: Provider | None = None,
    schema: str | Path | dict[str, Any] | list[Any] | None = None,
    system_prompt: str | None = None,
    document_id: str | None = None,
    max_tokens: int = 8192,
) -> ExtractionResult:
    """Extract structured JSON from a handwritten document."""
    document = normalize_input(source, document_id=document_id)
    schema_kind, schema_value = load_schema_guidance(schema)
    prompt = build_extraction_prompt(
        document_id=document.document_id,
        system_prompt=system_prompt,
        schema_kind=schema_kind,
        schema=schema_value,
    )

    active_provider = provider or LiteLLMProvider()
    response = active_provider.extract(document, prompt, model=model, max_tokens=max_tokens)
    data = parse_json_response(response.text)

    warnings: list[str] = []
    if schema_kind == "json_schema" and schema_value is not None:
        try:
            Draft202012Validator(schema_value).validate(data)
        except ValidationError as exc:
            warnings.append(f"Output did not validate against schema: {exc.message}")

    return ExtractionResult(
        document_id=document.document_id,
        data=data,
        provider=active_provider.name,
        model=model,
        usage=response.usage,
        warnings=warnings,
    )


def parse_json_response(text: str) -> dict[str, Any]:
    """Parse provider text into a JSON object."""
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned.removeprefix("```json").strip()
        cleaned = cleaned.removesuffix("```").strip()
    elif cleaned.startswith("```"):
        cleaned = cleaned.removeprefix("```").strip()
        cleaned = cleaned.removesuffix("```").strip()

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ResponseParseError(f"Provider returned invalid JSON: {exc.msg}") from exc

    if not isinstance(parsed, dict):
        raise ResponseParseError("Provider JSON response must be an object")

    return parsed
