from handwriting_json.prompts import build_extraction_prompt
from handwriting_json.schemas import load_schema_guidance


def test_detects_json_schema():
    kind, schema = load_schema_guidance({"type": "object", "properties": {"name": {"type": "string"}}})

    assert kind == "json_schema"
    assert schema["type"] == "object"


def test_detects_example_json():
    kind, schema = load_schema_guidance({"name": "", "medications": []})

    assert kind == "example"
    assert schema["name"] == ""


def test_prompt_includes_schema_guidance():
    prompt = build_extraction_prompt(
        document_id="sample.pdf",
        schema_kind="example",
        schema={"name": ""},
    )

    assert "sample.pdf" in prompt
    assert "example JSON" in prompt
    assert '"name": ""' in prompt
