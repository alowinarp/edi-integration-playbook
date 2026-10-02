# Standard Operating Procedures

An SOP in this repo defines the rules a team works to: the lifecycle, the standards, who does what, and the quality gates every change must pass.

## File naming

```
EDI-SOP-<NNN>_<Title>_v<major>.<minor>.pdf
```

| Part | Meaning |
|---|---|
| `EDI-SOP-<NNN>` | Permanent ID. Never reused. |
| `<Title>` | Short title, words joined by hyphens. |
| `v<major>` | Process change: a stage, gate, role, or standard changed. |
| `.<minor>` | Clarification or correction. The process itself is unchanged. |

Example: `EDI-SOP-001_EDI-Map-Development-Change-Management_v1.0.pdf`

## How an SOP is structured

Every SOP has the same core:

- Document control
- Purpose and scope
- Roles (RACI)
- Procedure: the stages or steps, each with entry and exit criteria
- Related templates
- Revision history

The remaining sections depend on the process the SOP governs. A development SOP adds development and testing standards. An incident management SOP adds severity levels, escalation paths, and response targets. Where a process is measured, the SOP defines its quality metrics. New SOPs add whatever sections their process needs.

## SOPs and templates

The SOP sets the rules and the gates. The [templates](../templates/) are the evidence each gate requires. Complete them per change and attach them to the change ticket. A gate without its completed template has not passed.

## Adapting an SOP

- Replace role names with your organization's titles. Keep the RACI assignments intact.
- Set your own metric targets. The values in each SOP are starting points.
- Map lifecycle stages to the statuses in your ticketing workflow.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE).

---

Back to the [repo overview](../README.md) · About the author and contact details are on that page.
