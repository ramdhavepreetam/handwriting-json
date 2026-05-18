# Examples

These examples show how to guide extraction for common handwritten-document automation workflows.

The core pattern is:

```bash
handwriting-json extract \
  --input handwritten_document.jpg \
  --schema examples/signup_form_schema.json \
  --model anthropic/claude-sonnet-4-5
```

## Included Schemas

- `signup_form_schema.json`: event signup, registration, or contact forms.
- `field_inspection_schema.json`: handwritten inspection notes and site reports.
- `school_permission_slip_schema.json`: school forms and permission slips.
- `donation_form_schema.json`: donation, pledge, or event contribution sheets.
- `clinic_intake_schema.json`: clinic intake paperwork.
- `prescription_schema.json`: prescription extraction as one healthcare example.

Do not commit real patient, customer, student, or private document data. Use synthetic examples only.
