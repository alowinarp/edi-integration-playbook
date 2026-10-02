# Templates

A template in this repo is the evidence a quality gate requires. The SOP sets the gate; the template proves it was passed.

## File naming

```
EDI-TPL-<NN>_<Title>_v<major>.<minor>.pdf
```

| Part | Meaning |
|---|---|
| `EDI-TPL-<NN>` | Permanent ID. Never reused. |
| `<Title>` | Short title, words joined by hyphens. |
| `v<major>` | Content change: a check or field was added, removed, or changed. |
| `.<minor>` | Clarification or correction. The checks and fields are unchanged. |

Example: `EDI-TPL-02_Peer-Review-Checklist_v1.0.pdf`

## How a template is structured

Every template has three parts:

- **Header:** what the record covers and why it exists. This identifies the work (change ticket, partner, transaction set, map, or monitoring period, as applicable) and the SOP and stage that require it.
- **Body:** the items to complete. Each item states what to verify or do and has a field for the result. The items differ by template.
- **Sign-off:** who completed it, who reviewed or approved it, the date, and the overall result.

## Using a template

- Complete one copy per change, per gate. Never reuse a completed copy across changes.
- Attach the completed copy to the change ticket before the gate is marked passed.
- Every item gets a result. Mark an item N/A only with a reason.
- A failed item blocks the gate until it is fixed and re-checked.

## Templates and SOPs

Each [SOP](../sop/) lists its templates under "Related templates." Each template's header names the SOP and stage it serves. The link runs both ways: any gate traces to its evidence, and any completed template traces back to its rule.

## Adapting a template

- Add your organization's own checks to the body.
- Keep the sign-off block. Without it, the template proves nothing.
- Match header field names to your ticketing system.
- Convert to a fillable form or a ticket checklist if that suits your workflow better.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE).

---

Back to the [repo overview](../README.md) · See the [SOPs](../sop/) for the gates these templates serve.