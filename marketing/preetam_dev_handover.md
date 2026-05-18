# Handwriting JSON Handover for Preetam.dev and Launch Marketing

Author: Preetam Ramdhave  
Project: Handwriting JSON  
Status: Published v0.1.0  
Date: May 17, 2026

## 1. Executive Summary

Handwriting JSON is an open-source Python package and CLI for schema-guided handwritten document extraction. It converts handwritten PDFs and images into structured JSON using vision LLMs and optional schema guidance.

The project grew out of OmmSai, a one-off healthcare automation project originally built to process roughly 15,000 handwritten prescription files for a charitable healthcare event. The public package generalizes that work beyond prescriptions into a reusable developer tool for forms, notes, surveys, field reports, medical documents, school paperwork, intake forms, and other handwritten records.

Core positioning:

> Schema-guided handwritten document extraction for developers.

Short pitch:

> Convert handwritten PDFs and images into structured JSON using vision LLMs and optional schema guidance.

## 2. Current Public Links

GitHub:

https://github.com/ramdhavepreetam/handwriting-json

PyPI:

https://pypi.org/project/handwriting-json/0.1.0/

TestPyPI:

https://test.pypi.org/project/handwriting-json/0.1.0/

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

## 3. Why This Project Exists

The original problem was practical: a charitable healthcare event had thousands of handwritten prescription documents that needed to become structured data. Manual transcription was too slow, too error-prone, and not realistic at that volume.

The broader problem is not limited to healthcare. Many teams still receive valuable operational data as handwritten documents: intake sheets, field notes, inspection forms, student forms, surveys, clinic forms, registration forms, and scanned records. OCR can return text, but applications need structured JSON that follows a predictable shape.

Handwriting JSON focuses on that gap:

- Input: messy handwritten PDFs/images.
- Guidance: optional JSON Schema or example JSON.
- Model: vision LLM routed through LiteLLM.
- Output: application-ready JSON.

The key insight:

> The problem is not just reading handwriting. The problem is turning ambiguous handwritten documents into structured data that software can reliably use.

## 4. What Is Published Today

Version: `0.1.0`

Published to:

- PyPI production.
- TestPyPI.
- GitHub public repository.

Verified:

- `pip install handwriting-json==0.1.0` from PyPI works.
- `import handwriting_json` works.
- `from handwriting_json import extract` works.
- `handwriting-json --help` works.
- `handwriting-json version` returns `0.1.0`.
- Test suite passes locally.

V1 capabilities:

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
- Prescription prompt preset.
- LiteLLM provider adapter.
- JSON response parsing and validation warnings.

V1 intentionally does not include:

- LangChain.
- LangGraph.
- Docker.
- REST API.
- OCR fallback.
- Hosted SaaS.
- Web frontend.

Reason:

> The first release should be a focused developer package that does one thing clearly: schema-guided handwritten document extraction.

## 5. Technical Architecture

Pipeline:

```text
input source -> normalized document -> prompt builder -> provider -> JSON parser -> optional schema validation -> result
```

Main package boundaries:

- `inputs`: normalizes paths, URLs, base64 strings, bytes, and file-like objects.
- `prompts`: builds generic and preset prompts.
- `schemas`: detects JSON Schema vs example JSON.
- `providers`: isolates model-provider calls behind a small interface.
- `extract`: public Python API and JSON parsing.
- `cli`: command-line interface.

Provider strategy:

- Use LiteLLM for routing across model providers.
- Avoid LangChain/LangGraph for v0.1 because this is not yet a multi-step agent workflow.
- Add orchestration later only if the product grows into retries, validation repair loops, OCR fallback, routing, and human review.

## 6. Developer Usage Examples

Python API:

```python
from handwriting_json import extract

result = extract(
    "registration_form.pdf",
    model="anthropic/claude-sonnet-4-5",
    schema={
        "full_name": "",
        "date": "",
        "phone": "",
        "items": []
    },
)

print(result.data)
```

CLI single document:

```bash
handwriting-json extract \
  --input form.pdf \
  --schema examples/form_schema.json \
  --output result.json \
  --model anthropic/claude-sonnet-4-5
```

CLI batch:

```bash
handwriting-json batch \
  --input-dir ./forms \
  --output results.jsonl \
  --model anthropic/claude-sonnet-4-5
```

Install from GitHub:

```bash
pip install git+https://github.com/ramdhavepreetam/handwriting-json.git
```

Install from PyPI:

```bash
pip install handwriting-json
```

## 7. Differentiation

Do not position this as only an OCR wrapper.

Better positioning:

- Schema-guided extraction.
- Developer-first handwritten document parsing.
- Vision LLM provider abstraction.
- Practical batch extraction foundation.
- Built from a real 15,000-document use case.

Comparison language:

- OCR gives text.
- Handwriting JSON gives structured JSON shaped for your application.
- OCR asks, "What text is visible?"
- Handwriting JSON asks, "What structured data should this document become?"

## 8. Ideal Audience

Primary:

- Developers building document automation pipelines.
- AI engineers prototyping vision LLM workflows.
- Founders or operators processing handwritten forms.
- Clinics, schools, NGOs, and small operations teams with paper workflows.

Secondary:

- Recruiters and hiring managers evaluating practical AI engineering work.
- Forward Deployed Engineering teams that value real-world automation.
- Open-source users looking for small, focused AI utilities.

## 9. Blog Article for Preetam.dev

Recommended title options:

1. From 15,000 Handwritten Prescriptions to an Open-Source Python Package
2. Why I Built Handwriting JSON: Schema-Guided Extraction for Handwritten Documents
3. OCR Is Not Enough: Turning Handwritten Forms into Structured JSON
4. Building Handwriting JSON: A Developer Tool for Messy Real-World Documents

Recommended final title:

> From 15,000 Handwritten Prescriptions to an Open-Source Python Package

Recommended subtitle:

> How a charity healthcare automation project became Handwriting JSON, a schema-guided Python package for turning handwritten PDFs and images into structured JSON.

Blog structure:

1. Hook: the 15,000-prescription origin story.
2. The real problem: handwritten documents are not application data.
3. Why OCR alone is not enough.
4. The design choice: schema-guided extraction.
5. Why provider abstraction matters.
6. Why I did not use LangChain or LangGraph for v0.1.
7. Package and CLI examples.
8. What is shipped today.
9. Roadmap.
10. Call to action: install, star GitHub, try it on a form, share feedback.

Suggested opening:

> I originally built OmmSai to process roughly 15,000 handwritten prescription files for a charitable healthcare event. The goal was simple: turn messy scanned prescriptions into structured data fast enough for people to actually use it. After the event, I realized the real problem was bigger than prescriptions. Teams everywhere still receive important data as handwritten forms, notes, and scans. OCR can read text, but most software needs JSON. So I refactored the idea into Handwriting JSON, an open-source Python package for schema-guided handwritten document extraction.

Suggested technical section:

> The key design choice is schema guidance. Without a schema, a vision model can describe a document, but the output may not be stable enough for software. With an example JSON object or JSON Schema, the model has a target shape. That turns the workflow from "read this image" into "extract this document into this data contract."

Suggested LangChain/LangGraph section:

> I intentionally avoided LangChain and LangGraph in v0.1. They are useful when you need multi-step orchestration, stateful agent workflows, tool routing, or graph execution. Handwriting JSON v0.1 is a focused extraction library: normalize input, build a prompt, call a vision model, parse JSON, validate if a schema exists. A small provider interface plus LiteLLM is enough for that job and keeps the package easier to install, understand, and maintain.

Suggested ending:

> This is early, but it is already installable from PyPI. If you have handwritten forms, scanned notes, or messy PDFs that need to become JSON, try it and send me the edge cases. The best open-source AI tools are built from real documents, not perfect demos.

## 10. LinkedIn Launch Strategy

Post 1: Launch story

Hook:

> I turned a tool I built for 15,000 handwritten prescriptions into an open-source Python package.

Body:

I originally built OmmSai for a charitable healthcare event that needed handwritten prescriptions converted into structured data.

The deeper lesson: the hard part was not just OCR. It was turning messy, ambiguous handwritten documents into JSON that downstream systems could trust.

So I refactored the idea into Handwriting JSON:

- PDFs/images in
- optional JSON Schema or example JSON
- vision LLM provider through LiteLLM
- structured JSON out
- Python API and CLI

Install:

```bash
pip install handwriting-json
```

GitHub:
https://github.com/ramdhavepreetam/handwriting-json

PyPI:
https://pypi.org/project/handwriting-json/

If you work with handwritten forms, clinic paperwork, field notes, surveys, or scanned records, I would love feedback.

Post 2: Technical design

Hook:

> OCR gives you text. Most applications need structured JSON.

Body points:

- OCR is useful but not sufficient.
- The product is schema-guided extraction.
- Example JSON guides the model toward a useful output shape.
- JSON Schema enables validation.
- LiteLLM keeps model choice open.
- V0.1 intentionally avoids heavy orchestration frameworks.

Post 3: Why no LangChain/LangGraph yet

Hook:

> I did not use LangChain or LangGraph in my new open-source AI package, and that was intentional.

Body points:

- The workflow is currently a single focused extraction path.
- Heavy orchestration would add complexity before it adds value.
- LiteLLM solves the provider abstraction problem directly.
- LangGraph may come later for validation repair, OCR fallback, routing, and human review.

Post 4: Build-in-public roadmap

Hook:

> V0.1 is live. Now the useful work starts.

Roadmap bullets:

- Better batch processing with checkpoints.
- Validation repair loop.
- Docker image.
- Cost reporting.
- More presets.
- Real-world examples from users.

## 11. GitHub README Improvements To Add Later

Add when time permits:

- Real demo GIF.
- Before/after document-to-JSON example.
- Badges for PyPI version, Python versions, license, tests.
- Provider setup section for Anthropic/OpenAI/Gemini.
- Copy-paste examples for common schemas.
- Troubleshooting section for invalid JSON and API keys.
- Roadmap checklist.

Suggested badges:

```md
![PyPI](https://img.shields.io/pypi/v/handwriting-json)
![Python](https://img.shields.io/pypi/pyversions/handwriting-json)
![License](https://img.shields.io/github/license/ramdhavepreetam/handwriting-json)
```

## 12. Launch Channels

Priority order:

1. LinkedIn launch post.
2. Preetam.dev blog article.
3. GitHub README polish.
4. Hacker News Show HN.
5. Reddit: r/Python, r/LocalLLaMA, r/MachineLearning if framed carefully.
6. Submit to awesome lists after the README has examples.
7. Follow-up LinkedIn technical posts.

Show HN title:

> Show HN: Handwriting JSON – Convert handwritten PDFs/images to structured JSON

Show HN body:

> I built this after working on a project that processed roughly 15,000 handwritten prescriptions for a charitable healthcare event. The package generalizes the idea: pass a handwritten PDF/image plus an optional JSON Schema or example JSON, and get structured JSON back using a vision LLM provider via LiteLLM. It is early, but installable from PyPI and usable as a Python package or CLI.

## 13. SEO Keywords

Primary:

- handwritten document extraction
- handwriting to JSON
- handwritten PDF to JSON
- schema-guided extraction
- AI document extraction Python
- vision LLM document extraction

Secondary:

- OCR to JSON
- handwritten forms automation
- document AI Python package
- extract structured data from handwritten forms
- handwritten prescription extraction
- LiteLLM vision extraction

## 14. Suggested Preetam.dev Integration

Current `preetam_dev` has a writing route and an existing OmmSai article stub:

- `/writing`
- `/writing/[slug]`
- existing slug: `ommsai-case-study`

Recommended site update:

- Add a new article slug: `handwriting-json-launch`.
- Keep the older OmmSai article as the origin story if desired.
- Add Handwriting JSON to the work/project grid as a separate open-source project.
- Link GitHub and PyPI prominently.

Recommended article metadata:

```ts
{
  title: "From 15,000 Handwritten Prescriptions to an Open-Source Python Package",
  description: "How I turned a charity healthcare automation project into Handwriting JSON, a schema-guided package for handwritten document extraction.",
  date: "May 17, 2026",
  readTime: "9 min read",
  slug: "handwriting-json-launch",
  tags: ["Open Source", "AI Engineering", "Python"]
}
```

Recommended project metadata:

```ts
{
  title: "Handwriting JSON",
  description: "Open-source Python package and CLI for schema-guided handwritten document extraction. Converts handwritten PDFs/images into structured JSON using vision LLMs and LiteLLM provider routing.",
  slug: "handwriting-json",
  tags: ["Python", "LiteLLM", "Document AI", "Open Source", "CLI"],
  metrics: "Published on PyPI",
  domain: "Open Source AI",
  github: "https://github.com/ramdhavepreetam/handwriting-json",
  url: "https://pypi.org/project/handwriting-json/"
}
```

## 15. FAQ For Marketing And Comments

Question: Is this OCR?

Answer: It uses vision LLMs for extraction. OCR returns text; Handwriting JSON focuses on structured JSON output guided by a schema or example object.

Question: Why LiteLLM?

Answer: LiteLLM gives provider flexibility without pulling in a full orchestration framework. Users can route to different vision-capable models while the package keeps a small API.

Question: Why not LangChain or LangGraph?

Answer: V0.1 is a focused extraction library. LangGraph may be useful later for validation repair loops, OCR fallback, routing, and human review workflows.

Question: Does it work with prescriptions?

Answer: Yes, prescriptions are supported as a preset/example, but the package is generic and intended for handwritten forms and documents broadly.

Question: Is it production-ready?

Answer: V0.1 is an early open-source release. It is installable from PyPI and usable as a Python package/CLI. Production use should add domain-specific validation and human review for high-risk fields.

Question: Can it run locally?

Answer: The package is local, but extraction depends on whichever vision LLM provider you configure through LiteLLM. Local model support can be added if LiteLLM/provider support is available.

## 16. Roadmap Talking Points

Near-term:

- Better batch mode with checkpoint/resume.
- Validation repair loop.
- Docker image.
- More schema examples.
- Provider setup docs.

Medium-term:

- OCR fallback.
- Cost reporting.
- Field-level confidence and evidence.
- Human review queue export.
- More domain presets.

Long-term:

- REST API mode.
- Hosted demo.
- Benchmark suite across handwriting document types.

## 17. Proof Points To Mention

- Published on PyPI.
- Public GitHub repository.
- Installable with one pip command.
- Originated from a real 15,000-document charitable healthcare use case.
- Provider-agnostic through LiteLLM.
- No LangChain/LangGraph dependency for v0.1 simplicity.
- Supports schema-guided extraction.

## 18. Recommended Calls To Action

For developers:

> Try it on one messy handwritten form and open an issue with the edge case.

For LinkedIn:

> If your team still receives data as handwritten PDFs or images, I would love to hear what document type is hardest to automate.

For GitHub:

> Star the repo if you want to follow the roadmap: validation repair, Docker, and checkpointed batch extraction.

For recruiters/FDE audience:

> This is the kind of practical AI engineering I want to do more of: take messy real-world workflows, build the automation layer, and make it usable by teams beyond the original use case.
