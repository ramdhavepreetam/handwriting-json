# Architecture

Handwriting JSON follows a small pipeline:

```text
input source -> normalized document -> prompt builder -> provider -> JSON parser -> optional validation -> result
```

## Package Boundaries

- `inputs`: normalize paths, URLs, base64 strings, bytes, and file-like objects.
- `prompts`: build generic and preset extraction prompts.
- `providers`: isolate model-provider calls behind a small interface.
- `schemas`: classify JSON Schema versus example JSON guidance.
- `extract`: public extraction API and response parsing.
- `cli`: Typer command-line interface.

## V1 Provider Strategy

The default provider uses LiteLLM. This keeps the package provider-agnostic without pulling in orchestration frameworks that are unnecessary for a single extraction call.
