"""LiteLLM-backed provider implementation."""

from __future__ import annotations

import base64
from typing import Any

from handwriting_json.errors import ProviderError
from handwriting_json.models import DocumentInput, ProviderResponse


class LiteLLMProvider:
    """Provider adapter that routes vision requests through LiteLLM."""

    name = "litellm"

    def __init__(self, **completion_kwargs: Any) -> None:
        self.completion_kwargs = completion_kwargs

    def extract(self, document: DocumentInput, prompt: str, *, model: str, max_tokens: int = 8192) -> ProviderResponse:
        try:
            from litellm import completion
        except ImportError as exc:
            raise ProviderError("LiteLLM is not installed. Install handwriting_json with its package dependencies.") from exc

        data_url = _to_data_url(document)
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            }
        ]

        try:
            response = completion(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                **self.completion_kwargs,
            )
        except Exception as exc:
            raise ProviderError(f"Provider request failed: {exc}") from exc

        try:
            text = response.choices[0].message.content
        except (AttributeError, IndexError, KeyError, TypeError) as exc:
            raise ProviderError("Provider response did not contain message text") from exc

        usage = getattr(response, "usage", None)
        usage_dict = usage.model_dump() if hasattr(usage, "model_dump") else dict(usage or {})
        return ProviderResponse(text=text, usage=usage_dict, raw=response)


def _to_data_url(document: DocumentInput) -> str:
    encoded = base64.b64encode(document.data).decode("ascii")
    return f"data:{document.media_type};base64,{encoded}"
