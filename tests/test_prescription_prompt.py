from handwriting_json.prompts import PRESCRIPTION_PROMPT


def test_prescription_prompt_is_available_as_preset():
    assert "prescription" in PRESCRIPTION_PROMPT.lower()
    assert "Return only valid JSON" in PRESCRIPTION_PROMPT
