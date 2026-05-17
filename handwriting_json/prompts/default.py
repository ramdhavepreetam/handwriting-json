"""Default prompt for generic handwritten document extraction."""

from __future__ import annotations

import json
from typing import Any

DEFAULT_SYSTEM_PROMPT = """You convert handwritten and printed documents into structured JSON.

Extract all visible information from the provided document. Preserve the original meaning and wording where possible. Do not invent missing values. If text is unreadable, use null and include a short note when that uncertainty matters.

Return only valid JSON. Do not wrap the response in markdown. Use stable field names in snake_case. Include confidence values when useful using: high, medium, low.
"""


def build_extraction_prompt(
    *,
    document_id: str,
    system_prompt: str | None = None,
    schema_kind: str | None = None,
    schema: Any | None = None,
) -> str:
    """Build the provider prompt for a document extraction request."""
    parts = [system_prompt or DEFAULT_SYSTEM_PROMPT]
    parts.append(f"\nDocument ID: {document_id}")

    if schema is not None:
        serialized = json.dumps(schema, indent=2, ensure_ascii=False)
        if schema_kind == "json_schema":
            parts.append(
                "\nUse this JSON Schema as the target output contract. "
                "Return JSON that conforms to it whenever the document contains the required information:\n"
                f"{serialized}"
            )
        else:
            parts.append(
                "\nUse this example JSON as the preferred output shape. "
                "Preserve the structure, but fill values from the document and use null for unreadable values:\n"
                f"{serialized}"
            )

    parts.append("\nReturn only the extracted JSON object.")
    return "\n".join(parts)
