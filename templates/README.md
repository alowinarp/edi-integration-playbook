# Templates

A template in this repo is the evidence a quality gate requires. The SOP sets the gate; the template proves it was passed.

## Templates in this folder

| ID | Template | Files | Completed by | SOP stage |
|---|---|---|---|---|
| EDI-TPL-01 | Test Scenarios and Results | [Template (.xlsx)](EDI-TPL-01_Test-Scenarios-and-Results_v1.0-Template.xlsx) · [Preview (PDF)](EDI-TPL-01_Test-Scenarios-and-Results_v1.0-Preview.pdf) | Map developer | Developer testing |
| EDI-TPL-02 | Peer Review Checklist | [PDF](EDI-TPL-02_Peer-Review-Checklist_v1.0.pdf) | Peer reviewer | Peer review |
| EDI-TPL-03 | Deployment Checklist | [PDF](EDI-TPL-03_Deployment-Checklist_v1.0.pdf) | Deployer | Deployment |

### EDI-TPL-01 — Test Scenarios and Results

Completed by the map developer during unit, integration and regression testing, then submitted with EDI-TPL-02 for peer review before promotion to PROD. Works with X12, EDIFACT and TRADACOMS.

The workbook has four tabs:

- **Overview:** the change, partner, EDI standard, message type, map and test environments.
- **Test Plan:** the five-step test execution flow, from test preparation to review.
- **Test Scenarios:** one row per scenario, with the expected result, actual result and PASS/FAIL status.
- **Appendix:** field descriptions with examples, and the drop-down list values.

The preview PDF shows a completed sample: a synthetic inbound X12 850 change with 16 scenarios across unit, integration and regression testing.

## File naming

```
EDI-TPL-<NN>_<Title>_v<major>.<minor>[-<Variant>].<ext>
```

| Part | Meaning |
|---|---|
| `EDI-TPL-<NN>` | Permanent ID. Never reused. |
| `<Title>` | Short title, words joined by hyphens. |
| `v<major>` | Content change: a check or field was added, removed, or changed. |
| `.<minor>` | Clarification or correction. The checks and fields are unchanged. |
| `-<Variant>` | Optional. `Template` for the blank editable file, `Preview` for a completed sample. Omitted when the template is published as a single file. |
| `<ext>` | `pdf` for printable checklists and previews, `xlsx` for editable workbooks. |

Examples:

- `EDI-TPL-02_Peer-Review-Checklist_v1.0.pdf`
- `EDI-TPL-01_Test-Scenarios-and-Results_v1.0-Template.xlsx`
- `EDI-TPL-01_Test-Scenarios-and-Results_v1.0-Preview.pdf`

## How a template is structured

Every template has three parts:

- **Header:** what the record covers and why it exists. This identifies the work (change ticket, partner, message type, map, or monitoring period, as applicable) and the SOP and stage that require it.
- **Body:** the items to complete. Each item states what to verify or do and has a field for the result. The items differ by template.
- **Sign-off:** who completed it, who reviewed or approved it, the date, and the overall result. For EDI-TPL-01, the developer and test date are recorded on the Overview tab, and review and approval are recorded on EDI-TPL-02.

## Using a template

- Complete one copy per change, per gate. Never reuse a completed copy across changes.
- Attach the completed copy to the change ticket before the gate is marked passed.
- Every item gets a result. On checklists, mark an item N/A only with a reason.
- A failed item blocks the gate until it is fixed and re-checked.

## Templates and SOPs

Each [SOP](../sop/) lists its templates under "Related templates." Each template names the SOP and stage it serves. The link runs both ways: any gate traces to its evidence, and any completed template traces back to its rule.

## Adapting a template

- Add your organization's own checks to the body.
- Keep the sign-off, whether on the template itself or on the review template that follows it. Without it, the template proves nothing.
- Match header field names to your ticketing system.
- In EDI-TPL-01, edit the drop-down values on the Appendix tab to match your test types.
- Convert to a fillable form or a ticket checklist if that suits your workflow better.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE).

---

Back to the [repo overview](../README.md) · See the [SOPs](../sop/) for the gates these templates serve.
