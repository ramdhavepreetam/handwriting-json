# LinkedIn Launch Post Draft

I just published Handwriting JSON, an open-source Python package for automating handwritten document workflows.

The idea is simple:

- handwritten PDFs/images in
- optional JSON Schema or example JSON
- vision LLM provider through LiteLLM
- automation-ready JSON out

Install:

```bash
pip install handwriting-json
```

Use it for handwritten signup sheets, field notes, inspection forms, school slips, donation forms, clinic intake paperwork, scanned records, and other paper workflows that still need to become software data.

This project was inspired by OmmSai, a tool I originally built around a charitable healthcare workflow involving roughly 15,000 handwritten prescription files. But prescriptions are only one example. The broader problem is everywhere: organizations still collect important information on paper, and software needs structured fields, not loose text.

OCR answers: "What text is visible?"

Handwriting JSON asks: "What structured JSON should this document become so automation can use it?"

GitHub:
https://github.com/ramdhavepreetam/handwriting-json

PyPI:
https://pypi.org/project/handwriting-json/

If your team still receives handwritten forms or scanned paperwork, I would love to hear what document type is hardest to automate.
