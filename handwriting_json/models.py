"""Shared models for document extraction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class DocumentInput:
    """Normalized document payload passed to providers."""

    document_id: str
    media_type: str
    data: bytes
    source: str
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def size_bytes(self) -> int:
        return len(self.data)


@dataclass(frozen=True)
class ProviderResponse:
    """Text and metadata returned by a provider."""

    text: str
    usage: dict[str, Any] = field(default_factory=dict)
    raw: Any | None = None


@dataclass(frozen=True)
class ExtractionResult:
    """Structured extraction result returned by the public API."""

    document_id: str
    data: dict[str, Any]
    provider: str
    model: str
    usage: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
