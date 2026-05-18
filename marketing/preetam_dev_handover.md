# Handwriting JSON Handover for Preetam.dev and Launch Marketing

Author: Preetam Ramdhave  
Project: Handwriting JSON  
Status: Published v0.1.1 positioning update  
Date: May 17, 2026

## 1. Executive Summary

Handwriting JSON is an open-source Python package and CLI for automating handwritten document workflows. It turns handwritten forms, notes, and scanned paperwork into automation-ready JSON using vision LLMs and optional schema guidance.

The project was inspired by OmmSai, a healthcare automation project that processed roughly 15,000 handwritten prescription files for a charitable healthcare event. That origin story is useful proof, but it should not define the product. The public product is broader: any handwritten document that needs to become structured data for software.

Core positioning:

> Turn handwriting into automation-ready JSON.

Expanded positioning:

> Handwriting JSON helps developers automate workflows that still depend on handwritten forms, notes, and scanned paperwork.

Short pitch:

> Convert handwritten PDFs/images into structured JSON using vision LLMs and optional schema guidance.

## 2. Public Links

GitHub:

https://github.com/ramdhavepreetam/handwriting-json

PyPI:

https://pypi.org/project/handwriting-json/

Install:

```bash
pip install handwriting-json
```

Import:

```python
from handwriting_json import extract
```

CLI:

```bash
handwriting-json --help
handwriting-json version
```

## 3. The Market Problem

Many organizations still collect important data on paper:

- registration forms
- field inspection notes
- school permission slips
- donation forms
- clinic intake forms
- KYC forms
- survey sheets
- maintenance reports
- delivery notes
- meeting notes
- lab slips
- old scanned records

OCR can return text, but automation usually needs fields. A CRM, ticketing system, spreadsheet import, compliance workflow, student database, or review queue needs structured JSON.

The key message:

> The hard part is not just reading handwriting. The hard part is turning handwritten documents into data that software can act on.

## 4. Product Framing

Do lead with:

- handwritten workflow automation
- automation-ready JSON
- schema-guided extraction
- forms, notes, and scanned paperwork
- developer-friendly Python API and CLI
- provider flexibility through LiteLLM

Do not lead with:

- prescriptions
- OCR wrapper
- medical-only use case
- LangChain/LangGraph

Use prescriptions as proof:

> Inspired by a real healthcare workflow involving roughly 15,000 handwritten prescription files.

## 5. What Is Published

Version: `0.1.1` planned/published after positioning update.

Already verified for v0.1.0:

- PyPI install works.
- TestPyPI install works.
- GitHub repository is public.
- Python import works.
- CLI works.

V0.1.x capabilities:

- Python package.
- Typer CLI.
- Local path input.
- URL input.
- Base64 input.
- Bytes and file-like object input through Python API.
- PDF, PNG, JPG/JPEG, and WebP detection.
- JSON Schema guidance.
- Example JSON guidance.
- Generic default extraction prompt.
- Multiple generic schema examples.
- Prescription prompt preset as one domain example.
- LiteLLM provider adapter.
- JSON response parsing and validation warnings.

Intentional non-goals for now:

- LangChain.
- LangGraph.
- Docker.
- REST API.
- OCR fallback.
- Hosted SaaS.
- Web frontend.

## 6. Usage Examples

Python API:

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

Field inspection example:

```python
result = extract(
    "inspection_note.jpg",
    model="anthropic/claude-sonnet-4-5",
    schema={
        "site_name": "",
        "inspection_date": "",
        "inspector": "",
        "issues": [],
        "recommended_action": "",
        "urgency": ""
    },
)
```

CLI:

```bash
handwriting-json extract \
  --input handwritten_signup_form.jpg \
  --schema examples/signup_form_schema.json \
  --output result.json \
  --model anthropic/claude-sonnet-4-5
```

## 7. Blog Article for Preetam.dev

Recommended title:

> Turning Handwritten Forms into Automation-Ready JSON

Alternative titles:

1. OCR Is Not Enough: Turning Handwritten Forms into Structured JSON
2. From Paper Workflows to JSON: Why I Built Handwriting JSON
3. Automating Handwritten Documents with Vision LLMs and Schema Guidance
4. From 15,000 Prescriptions to a General Handwriting Automation Package

Recommended subtitle:

> How a healthcare automation project became a general-purpose Python package for turning handwritten forms, notes, and scanned paperwork into structured JSON.

Recommended article structure:

1. Start with the broad pain: every organization still has paper workflows.
2. Use OmmSai and the 15,000-prescription project as the origin story.
3. Explain why the problem is broader than healthcare.
4. Explain why OCR alone is not enough.
5. Introduce schema-guided extraction.
6. Show Python and CLI examples.
7. Explain LiteLLM and provider flexibility.
8. Explain why LangChain/LangGraph are deferred.
9. Show roadmap.
10. Ask readers for real document edge cases.

Suggested opening:

> Every organization has at least one workflow that still starts on paper: a registration form, an inspection note, a school slip, a donation sheet, a clinic intake form, a scanned record. The problem is not only reading the handwriting. The real problem is turning that handwriting into structured data that software can use.
>
> I first ran into this through OmmSai, a healthcare automation project built around roughly 15,000 handwritten prescription files for a charitable healthcare event. After that project, I realized prescriptions were only one instance of a much broader pattern. So I built Handwriting JSON: an open-source Python package and CLI for turning handwritten forms, notes, and scanned paperwork into automation-ready JSON.

Suggested technical section:

> The key design choice is schema guidance. Without a schema, a vision model can describe a document, but the output may not be stable enough for automation. With an example JSON object or JSON Schema, the model has a target contract. The workflow changes from "read this image" to "extract this document into this shape."

Suggested ending:

> Handwriting JSON is early, but it is live on PyPI. If your team has handwritten forms, scanned notes, or paper workflows that should become software data, try it and send me the edge cases. The best version of this project will come from messy real documents, not perfect demos.

## 8. LinkedIn Launch Post

Hook:

> I just published an open-source Python package for turning handwritten forms into automation-ready JSON.

Body:

Every organization has paper workflows: registration forms, inspection notes, school slips, donation sheets, clinic intake forms, scanned records.

OCR can give you text. But automation needs structured fields.

So I built Handwriting JSON:

- handwritten PDFs/images in
- optional JSON Schema or example JSON
- vision LLM provider through LiteLLM
- structured JSON out
- Python API and CLI

Install:

```bash
pip install handwriting-json
```

This project was inspired by OmmSai, a healthcare automation project involving roughly 15,000 handwritten prescription files. But the package is intentionally broader: prescriptions are one example, not the product boundary.

GitHub:
https://github.com/ramdhavepreetam/handwriting-json

PyPI:
https://pypi.org/project/handwriting-json/

If your team still receives handwritten forms or scanned paperwork, I would love to know what document type is hardest to automate.

## 9. Follow-Up LinkedIn Posts

Post 2: OCR vs automation-ready JSON

Hook:

> OCR gives you text. Most workflows need fields.

Points:

- Text extraction is not enough for CRM/ticketing/spreadsheet workflows.
- Schema guidance gives the model a target structure.
- JSON output can flow into automation.

Post 3: Why LiteLLM, not LangChain/LangGraph

Hook:

> I did not add LangChain or LangGraph to my handwritten document extraction package, and that was intentional.

Points:

- V0.1 is a focused extraction primitive.
- LiteLLM solves provider routing.
- Orchestration frameworks become useful later for repair loops, routing, OCR fallback, and human review.

Post 4: Use-case thread

Hook:

> 10 paper workflows that should become JSON.

List:

- signup forms to CRM
- field notes to tickets
- inspection sheets to compliance reports
- permission slips to student records
- donation forms to spreadsheets
- intake forms to review queues
- KYC forms to onboarding systems
- maintenance reports to work orders
- delivery notes to operations logs
- scanned records to searchable JSON

## 10. SEO Keywords

Primary:

- handwritten forms to JSON
- handwriting to JSON
- handwritten document automation
- handwritten PDF to JSON
- schema-guided document extraction
- vision LLM document extraction
- AI document extraction Python

Secondary:

- OCR to JSON
- automate handwritten forms
- handwritten paperwork automation
- scanned paperwork to JSON
- document AI Python package
- extract structured data from handwritten forms
- LiteLLM vision extraction

## 11. Suggested Preetam.dev Updates

Writing article metadata:

```ts
{
  title: "Turning Handwritten Forms into Automation-Ready JSON",
  description: "How I turned a healthcare automation project into Handwriting JSON, an open-source Python package for automating handwritten forms, notes, and scanned paperwork.",
  date: "May 17, 2026",
  readTime: "9 min read",
  slug: "handwriting-json-launch",
  tags: ["Open Source", "AI Engineering", "Python"]
}
```

Project metadata:

```ts
{
  title: "Handwriting JSON",
  description: "Open-source Python package and CLI for automating handwritten document workflows. Converts forms, notes, and scanned paperwork into structured JSON using vision LLMs and optional schema guidance.",
  slug: "handwriting-json",
  tags: ["Python", "LiteLLM", "Document AI", "Open Source", "CLI"],
  metrics: "Published on PyPI",
  domain: "Open Source AI",
  github: "https://github.com/ramdhavepreetam/handwriting-json",
  url: "https://pypi.org/project/handwriting-json/"
}
```

## 12. FAQ

Question: Is this OCR?

Answer: It uses vision LLMs for extraction. OCR returns text; Handwriting JSON focuses on structured JSON output guided by a schema or example object.

Question: What can I automate with it?

Answer: Signup forms, field notes, inspection sheets, permission slips, donation forms, clinic intake paperwork, KYC forms, surveys, maintenance notes, delivery slips, scanned records, and similar handwritten workflows.

Question: Does it only work for prescriptions?

Answer: No. Prescriptions are one healthcare example and part of the origin story. The package is generic.

Question: Why LiteLLM?

Answer: LiteLLM provides model-provider flexibility without adding a heavy orchestration layer.

Question: Why not LangChain or LangGraph?

Answer: V0.1 is a focused extraction library. LangGraph may be useful later for validation repair loops, OCR fallback, document routing, and human review workflows.

Question: Is it production-ready?

Answer: It is an early package release. Production workflows should add domain-specific validation and human review for high-risk fields.

## 13. Calls To Action

For developers:

> Try it on one handwritten form and open an issue with the edge case.

For LinkedIn:

> What handwritten workflow at your company should already be automated?

For GitHub:

> Star the repo to follow the roadmap: validation repair, checkpointed batch processing, Docker, and field-level evidence.

For FDE positioning:

> This is the kind of AI engineering I want to do more of: take messy real-world workflows, build the automation layer, and make it usable beyond the original customer or event.
