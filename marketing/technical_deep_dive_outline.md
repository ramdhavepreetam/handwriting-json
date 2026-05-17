# Technical Deep Dive Outline

## Working title

From 15,000 handwritten prescriptions to a generic document extraction package

## Sections

1. The original problem: charitable healthcare event paperwork at scale.
2. Why OCR alone is not enough for structured extraction.
3. Schema-guided prompting as the core design choice.
4. Why LiteLLM instead of LangChain/LangGraph for V1.
5. Batch processing lessons: retries, checkpoints, failures, cost.
6. What is next: validation repair loop, Docker, and field-level evidence.
