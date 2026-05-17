import pytest

from handwriting_json.errors import ResponseParseError
from handwriting_json.extract import extract, parse_json_response
from handwriting_json.models import ProviderResponse


class FakeProvider:
    name = "fake"

    def __init__(self, text='{"patient_name": "John Doe"}'):
        self.text = text
        self.last_prompt = None

    def extract(self, document, prompt, *, model, max_tokens):
        self.last_prompt = prompt
        return ProviderResponse(text=self.text, usage={"input_tokens": 1, "output_tokens": 2})


def test_extract_with_fake_provider(tmp_path):
    pdf = tmp_path / "sample.pdf"
    pdf.write_bytes(b"%PDF-1.4\n%test\n")
    provider = FakeProvider()

    result = extract(pdf, model="test-model", provider=provider, schema={"patient_name": ""})

    assert result.document_id == "sample.pdf"
    assert result.provider == "fake"
    assert result.model == "test-model"
    assert result.data["patient_name"] == "John Doe"
    assert "example JSON" in provider.last_prompt


def test_parse_json_response_strips_markdown():
    assert parse_json_response('```json\n{"ok": true}\n```') == {"ok": True}


def test_parse_json_response_requires_object():
    with pytest.raises(ResponseParseError):
        parse_json_response("[1, 2, 3]")
