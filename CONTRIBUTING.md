# Contributing

Thanks for your interest in Handwriting JSON.

## Development Setup

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest tests
```

## Contribution Guidelines

- Keep the core package generic; domain-specific behavior should live in examples or presets.
- Do not add LangChain or LangGraph for V1 features unless there is a concrete multi-step workflow requirement.
- Add tests for input handling, prompt construction, schema behavior, provider parsing, and CLI behavior.
- Do not commit real documents, credentials, API keys, generated extraction output, or patient/user data.

## Pull Request Checklist

- Tests pass with `python3 -m pytest tests`.
- Public API changes are reflected in the README.
- New examples use synthetic or sanitized data only.
