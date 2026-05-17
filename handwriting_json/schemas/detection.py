"""Load and classify optional schema guidance."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Literal

from jsonschema import Draft202012Validator, SchemaError as JsonSchemaError

from handwriting_json.errors import SchemaError

SchemaKind = Literal["json_schema", "example"]


def load_schema_guidance(schema: str | Path | dict[str, Any] | list[Any] | None) -> tuple[SchemaKind | None, Any | None]:
    """Load schema guidance from a path, JSON string, dict/list, or None."""
    if schema is None:
        return None, None

    loaded = _load_schema_value(schema)
    kind: SchemaKind = "json_schema" if _looks_like_json_schema(loaded) else "example"

    if kind == "json_schema":
        try:
            Draft202012Validator.check_schema(loaded)
        except JsonSchemaError as exc:
            raise SchemaError(f"Invalid JSON Schema: {exc.message}") from exc

    return kind, loaded


def _load_schema_value(schema: str | Path | dict[str, Any] | list[Any]) -> Any:
    if isinstance(schema, Path):
        return _read_json_file(schema)

    if isinstance(schema, (dict, list)):
        return schema

    if isinstance(schema, str):
        path = Path(schema).expanduser()
        if path.exists():
            return _read_json_file(path)
        try:
            return json.loads(schema)
        except json.JSONDecodeError as exc:
            raise SchemaError("Schema must be a JSON object, JSON array, JSON string, or path to a JSON file") from exc

    raise SchemaError(f"Unsupported schema type: {type(schema).__name__}")


def _read_json_file(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise SchemaError(f"Could not read schema file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SchemaError(f"Schema file is not valid JSON: {path}") from exc


def _looks_like_json_schema(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    schema_keys = {"$schema", "$id", "type", "properties", "required", "additionalProperties"}
    return bool(schema_keys.intersection(value))
