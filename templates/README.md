# Templates

A template in this repo is the evidence a quality gate requires. The SOP sets the gate; the template proves it was passed.

## Finding a template

Every template in this folder is in the file list above, sorted by ID. To find the template for a gate:

- **Start from the SOP.** Each SOP lists the templates it requires under "Related templates."
- **Or start from the template.** Each template's How to Use tab or header names the SOP stage it serves and who completes it.

When a template has both a blank file and a completed sample, they share an ID and title. Fill in the `-Template` file. The `-Preview` file shows a completed example.

## File naming

```
EDI-TPL-<NN>_<Title>[-<Variant>].<ext>
```

| Part | Meaning |
|---|---|
| `EDI-TPL-<NN>` | Permanent ID. Never reused. |
| `<Title>` | Short title, words joined by hyphens. |
| `-<Variant>` | Optional. `Template` for the blank editable file, `Preview` for a completed sample. Omitted when the template is published as a single file. |
| `<ext>` | `pdf` for printable checklists and previews, `xlsx` for editable workbooks. |

Examples:

- `EDI-TPL-01_Test-Scenarios-and-Results-Template.xlsx`
- `EDI-TPL-01_Test-Scenarios-and-Results-Preview.pdf`

Filenames carry no version number, so links stay stable across updates.

## Versions

The current version is printed in the page footer, with the template ID and title, on every printed page and PDF.

| Change | Meaning |
|---|---|
| `v<major>` | Content change: a check or field was added, removed, or changed. |
| `.<minor>` | Clarification, correction, or layout change. The checks and fields are unchanged. |

The full change history is in the repository's commit log.

## How a template is structured

Every template has three parts:

- **Header:** what the record covers and why it exists. This identifies the work (change ticket, partner, message type, map, or monitoring period, as applicable) and the SOP stage that requires it.
- **Body:** the items to complete. Each item states what to verify or do and has a field for the result. The items differ by template.
- **Sign-off:** who completed it, who reviewed or approved it, the date, and the overall result. For EDI-TPL-01, the developer and test date are recorded on the Overview tab, and review and approval are recorded on EDI-TPL-02.

Workbook templates open on a **How to Use** tab: the purpose, when the template starts and ends, who completes it, and the steps.

## Using a template

- Complete one copy per change, per gate. Never reuse a completed copy across changes.
- Attach the completed copy to the change ticket before the gate is marked passed.
- Every item gets a result. On checklists, mark an item N/A only with a reason.
- A failed item blocks the gate until it is fixed and re-checked.

## Templates and SOPs

Each [SOP](../sop/) lists its templates under "Related templates." Each template names the SOP stage it serves. The link runs both ways: any gate traces to its evidence, and any completed template traces back to its rule.

## Adapting a template

- Add your organization's own checks to the body.
- Keep the sign-off, whether on the template itself or on the review template that follows it. Without it, the template proves nothing.
- Match header field names to your ticketing system.
- In workbook templates, edit the drop-down values on the Appendix tab to match your own test types and statuses.
- Convert to a fillable form or a ticket checklist if that suits your workflow better.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE).

---

Back to the [repo overview](../README.md) · See the [SOPs](../sop/) for the gates these templates serve.
