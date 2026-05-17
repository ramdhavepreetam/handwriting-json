import base64

import pytest

from handwriting_json.errors import InputError
from handwriting_json.inputs import normalize_input


def test_normalize_pdf_path(tmp_path):
    pdf = tmp_path / "sample.pdf"
    pdf.write_bytes(b"%PDF-1.4\n%test\n")

    document = normalize_input(pdf)

    assert document.document_id == "sample.pdf"
    assert document.media_type == "application/pdf"
    assert document.size_bytes > 0


def test_normalize_base64_data_url():
    encoded = base64.b64encode(b"%PDF-1.4\n%test\n").decode("ascii")

    document = normalize_input(f"data:application/pdf;base64,{encoded}", document_id="inline.pdf")

    assert document.document_id == "inline.pdf"
    assert document.media_type == "application/pdf"


def test_rejects_unknown_input():
    with pytest.raises(InputError):
        normalize_input("not a path and not base64")
