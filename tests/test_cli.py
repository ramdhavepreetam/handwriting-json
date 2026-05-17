from typer.testing import CliRunner

from handwriting_json.cli import app


def test_cli_version():
    result = CliRunner().invoke(app, ["version"])

    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_cli_exposes_extract_and_batch():
    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "extract" in result.output
    assert "batch" in result.output
