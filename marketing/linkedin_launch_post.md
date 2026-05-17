# LinkedIn Launch Post Draft

I originally built a tool to process roughly 15,000 handwritten prescriptions for a charitable healthcare event.

The hard part was not just reading handwriting. The hard part was turning messy scanned documents into reliable, structured JSON that another system could use.

I am now open-sourcing the generalized version: Handwriting JSON.

It is a Python package and CLI for schema-guided handwritten document extraction:

- PDFs/images in
- optional JSON schema or example shape
- vision LLM provider of your choice through LiteLLM
- structured JSON out

GitHub: https://github.com/ramdhavepreetam/handwriting-json
