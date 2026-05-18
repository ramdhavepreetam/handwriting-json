# Architecture

Handwriting JSON follows a small automation-oriented pipeline:

```text
handwritten document -> normalized input -> schema-guided prompt -> vision LLM provider -> JSON parser -> optional validation -> automation-ready result
```

## Package Boundaries

- `inputs`: normalize paths, URLs, base64 strings, bytes, and file-like objects.
- `prompts`: build generic and preset extraction prompts.
- `providers`: isolate model-provider calls behind a small interface.
- `schemas`: classify JSON Schema versus example JSON guidance.
- `extract`: public extraction API and response parsing.
- `cli`: Typer command-line interface.

## V0.1 Provider Strategy

The default provider uses LiteLLM. This keeps the package provider-agnostic without pulling in orchestration frameworks that are unnecessary for a single extraction call.

LangChain and LangGraph are intentionally out of scope for v0.1. They may become useful later if the package adds multi-step workflows such as OCR fallback, validation repair loops, document-type routing, or human review.

## Automation Model

The package is designed to sit before downstream systems:

- form to CRM record
- inspection note to ticket
- school slip to student database
- donation form to spreadsheet
- clinic intake form to review queue
- handwritten record to JSONL batch output

V0.1 provides the extraction primitive. Later versions can add stronger batch reliability, repair loops, and workflow adapters.
