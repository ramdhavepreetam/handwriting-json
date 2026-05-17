"""Provider protocol."""

from __future__ import annotations

from typing import Protocol

from handwriting_json.models import DocumentInput, ProviderResponse


class Provider(Protocol):
    """Vision LLM provider interface."""

    name: str

    def extract(self, document: DocumentInput, prompt: str, *, model: str, max_tokens: int) -> ProviderResponse:
        """Return provider text for the given document and prompt."""
