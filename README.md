# Handwriting JSON

Turn handwritten forms, notes, and scanned paperwork into automation-ready JSON.

Handwriting JSON is a Python package and CLI for automating handwritten document workflows. It uses vision LLMs and optional schema guidance to convert PDFs/images into structured JSON your applications can use.

It is built for the messy documents that still slow teams down: registration forms, field notes, inspection sheets, school permission slips, donation forms, clinic intake paperwork, KYC forms, surveys, maintenance reports, delivery notes, lab slips, and old scanned records.

The project was inspired by OmmSai, a healthcare automation project that processed roughly 15,000 handwritten prescription files for a charitable healthcare event. Prescriptions are now just one example. The package is designed for many handwritten-document automation workflows.

## Why It Exists

Many business workflows still start with paper. A person fills out a form, writes a note, signs a slip, or scans an old record. OCR can return text, but automation usually needs structured data.

Handwriting JSON focuses on the automation step:

```text
handwritten document -> schema-guided extraction -> structured JSON -> downstream workflow
```

Use it to turn:

- handwritten signup sheets into CRM records
- field notes into tickets
- inspection forms into compliance reports
- school slips into student records
- donation forms into spreadsheets
- clinic intake forms into review queues
- scanned records into searchable JSON

## Features

- Extract structured JSON from handwritten PDFs and images.
- Guide extraction with JSON Schema or an example JSON object.
- Use multiple vision LLM providers through LiteLLM.
- Process one document or a directory of documents from the CLI.
- Use the same extraction path from Python code or the command line.
- Keep domain-specific behavior in examples and presets.

## Install

```bash
pip install handwriting-json
```

Provider credentials are configured through the environment variables expected by LiteLLM for the model you choose.

For local development:

```bash
git clone https://github.com/ramdhavepreetam/handwriting-json.git
cd handwriting-json
python3 -m pip install -e ".[dev]"
```

## Python API

```python
from handwriting_json import extract

result = extract(
    "handwritten_registration_form.jpg",
    model="anthropic/claude-sonnet-4-5",
    schema={
        "full_name": "",
        "phone": "",
        "email": "",
        "address": "",
        "date": "",
        "notes": "",
        "signature_present": False
    },
)

print(result.data)
```

## CLI

```bash
handwriting-json extract \
  --input handwritten_signup_form.jpg \
  --schema examples/signup_form_schema.json \
  --output result.json \
  --model anthropic/claude-sonnet-4-5
```

Batch mode:

```bash
handwriting-json batch \
  --input-dir ./forms \
  --output results.jsonl \
  --model anthropic/claude-sonnet-4-5
```

Check installation:

```bash
handwriting-json version
python3 -m handwriting_json --help
```

## Example Schemas

Registration form:

```json
{
  "full_name": "",
  "phone": "",
  "email": "",
  "address": "",
  "date": "",
  "notes": "",
  "signature_present": false
}
```

Field inspection note:

```json
{
  "site_name": "",
  "inspection_date": "",
  "inspector": "",
  "issues": [],
  "recommended_action": "",
  "urgency": ""
}
```

School permission slip:

```json
{
  "student_name": "",
  "parent_name": "",
  "class": "",
  "event": "",
  "consent_given": false,
  "emergency_contact": ""
}
```

More examples live in [`examples/`](examples/).

## Schema Guidance

You can pass either:

- a formal JSON Schema, or
- a simpler example JSON object.

The schema is injected into the prompt so the model knows the desired output shape. Formal JSON Schema responses are also validated after extraction.

## Why This Is Not Just OCR

OCR asks:

> What text is visible?

Handwriting JSON asks:

> What structured data should this document become so software can use it?

That distinction matters for automation. A CRM, ticketing system, spreadsheet import, compliance workflow, or review queue does not need a paragraph of text. It needs fields.

## Why LiteLLM, Not LangChain/LangGraph?

V0.1 is a focused extraction library: normalize input, build a schema-guided prompt, call a vision model, parse JSON, and optionally validate the output.

LiteLLM solves the provider-routing problem without adding orchestration complexity. LangChain or LangGraph may become useful later for multi-step workflows such as OCR fallback, validation repair loops, routing by document type, and human review queues.

## Roadmap

- V0.1: Python package, CLI, schema guidance, LiteLLM provider abstraction.
- V0.1.x: stronger examples, provider setup docs, README demos.
- V0.2: checkpointed batch processing and validation repair loop.
- Later: Docker image, REST API mode, OCR fallback, cost reporting, field-level evidence.

## Links

- GitHub: https://github.com/ramdhavepreetam/handwriting-json
- PyPI: https://pypi.org/project/handwriting-json/

## License

MIT
