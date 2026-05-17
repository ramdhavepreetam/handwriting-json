"""Command-line interface for Handwriting JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from handwriting_json import __version__
from handwriting_json.errors import HandwritingJsonError
from handwriting_json.extract import extract

app = typer.Typer(help="Convert handwritten documents into structured JSON.")


@app.command("extract")
def extract_command(
    input: Path = typer.Option(..., "--input", "-i", exists=True, readable=True, help="PDF or image to extract."),
    model: str = typer.Option(..., "--model", "-m", help="Vision-capable model name routed by LiteLLM."),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Write JSON result to this path."),
    schema: Optional[Path] = typer.Option(None, "--schema", "-s", exists=True, readable=True, help="JSON Schema or example JSON file."),
    max_tokens: int = typer.Option(8192, "--max-tokens", min=1, help="Maximum provider output tokens."),
) -> None:
    """Extract one document."""
    try:
        result = extract(input, model=model, schema=schema, max_tokens=max_tokens)
    except HandwritingJsonError as exc:
        raise typer.BadParameter(str(exc)) from exc

    payload = {
        "document_id": result.document_id,
        "data": result.data,
        "provider": result.provider,
        "model": result.model,
        "usage": result.usage,
        "warnings": result.warnings,
    }
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)

    if output:
        output.write_text(rendered + "\n", encoding="utf-8")
    else:
        typer.echo(rendered)


@app.command()
def batch(
    input_dir: Path = typer.Option(..., "--input-dir", "-i", exists=True, file_okay=False, readable=True, help="Directory of PDFs/images."),
    model: str = typer.Option(..., "--model", "-m", help="Vision-capable model name routed by LiteLLM."),
    output: Path = typer.Option(..., "--output", "-o", help="Write JSONL batch results to this path."),
    schema: Optional[Path] = typer.Option(None, "--schema", "-s", exists=True, readable=True, help="JSON Schema or example JSON file."),
    max_tokens: int = typer.Option(8192, "--max-tokens", min=1, help="Maximum provider output tokens per document."),
) -> None:
    """Extract every supported document in a directory."""
    supported_suffixes = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
    inputs = sorted(path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() in supported_suffixes)

    with output.open("w", encoding="utf-8") as output_file:
        for path in inputs:
            try:
                result = extract(path, model=model, schema=schema, max_tokens=max_tokens)
                payload = {
                    "document_id": result.document_id,
                    "data": result.data,
                    "provider": result.provider,
                    "model": result.model,
                    "usage": result.usage,
                    "warnings": result.warnings,
                }
            except HandwritingJsonError as exc:
                payload = {
                    "document_id": path.name,
                    "error": str(exc),
                }
            output_file.write(json.dumps(payload, ensure_ascii=False) + "\n")

    typer.echo(f"Processed {len(inputs)} file(s). Results written to {output}")


@app.command()
def version() -> None:
    """Print the installed Handwriting JSON version."""
    typer.echo(__version__)


if __name__ == "__main__":
    app()
