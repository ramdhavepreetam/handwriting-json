# Technical Deep Dive Outline

## Working title

OCR Is Not Enough: Turning Handwritten Forms into Automation-Ready JSON

## Thesis

The hard part is not simply reading handwriting. The hard part is turning ambiguous handwritten documents into structured data that downstream software can trust.

## Sections

1. Origin: from a 15,000-document healthcare workflow to a generic automation package.
2. The broader problem: handwritten forms, notes, slips, sheets, and records still drive real workflows.
3. Why OCR alone is not enough for automation.
4. Schema-guided extraction: example JSON and JSON Schema as target contracts.
5. Provider abstraction: why LiteLLM is enough for v0.1.
6. Why LangChain/LangGraph are intentionally deferred.
7. CLI and Python API examples.
8. Roadmap: validation repair, checkpointed batch, Docker, OCR fallback.
