# Handwriting JSON

Schema-guided handwritten document extraction for developers.

Handwriting JSON converts handwritten PDFs and images into structured JSON using vision LLMs and optional schema guidance. It is provider-agnostic through LiteLLM, so you can route extraction through models from Anthropic, OpenAI, Gemini, Mistral, and other supported providers.

Originally, this project came from OmmSai, a prescription extraction system built to process roughly 15,000 handwritten prescription files for a charitable healthcare event. This repository generalizes that work into a clean open-source Python package and CLI.

## Features

- Extract structured JSON from handwritten PDFs and images.
- Guide extraction with JSON Schema or an example JSON object.
- Use multiple vision LLM providers through LiteLLM.
- Process one document or a directory of documents from the CLI.
- Use the same extraction path from Python code or the command line.
- Keep prescription extraction as an optional preset, not the product boundary.

## Install

```bash
pip install handwriting-json
```

For local development:

```bash
git clone https://github.com/ramdhavepreetam/handwriting-json.git
cd handwriting-json
python3 -m pip install -e ".[dev]"
```

Provider credentials are configured through the environment variables expected by LiteLLM for the model you choose.

## Python API

```python
from handwriting_json import extract

result = extract(
    "examples/sample.pdf",
    model="anthropic/claude-sonnet-4-5",
    schema={
        "name": "",
        "date": "",
        "items": []
    },
)

print(result.data)
```

## CLI

```bash
handwriting-json extract --input form.pdf --model anthropic/claude-sonnet-4-5
handwriting-json extract --input form.pdf --schema examples/form_schema.json --output result.json --model anthropic/claude-sonnet-4-5
handwriting-json batch --input-dir ./forms --output results.jsonl --model anthropic/claude-sonnet-4-5
handwriting-json version
```

During development, the module form also works:

```bash
python3 -m handwriting_json --help
```

## Schema Guidance

You can pass a formal JSON Schema or a simpler example JSON object.

```json
{
  "name": "",
  "date": "",
  "items": [
    {
      "label": "",
      "value": "",
      "confidence": ""
    }
  ]
}
```

The schema is injected into the prompt so the model knows the desired output shape. Formal JSON Schema responses are also validated after extraction.

## Positioning

This is not just OCR. The goal is schema-guided handwritten document extraction: turning messy handwritten documents into application-ready JSON.

Good use cases include intake forms, field notes, inspection sheets, surveys, prescriptions, school forms, KYC forms, and scanned operational paperwork.

## Development Checks

```bash
python3 -m pytest tests
python3 -m handwriting_json --help
python3 -m handwriting_json version
```

## Roadmap

- V1: Python package, CLI, schema guidance, LiteLLM provider abstraction.
- V1.1: checkpointed batch processing, validation repair loop, Docker image.
- Later: REST API mode, OCR fallback, cost reporting, more domain presets.

## License

MIT
