# Standard Operating Procedures

An SOP in this repo defines the rules a team works to: the lifecycle, the standards, who does what, and the quality gates every change must pass. The SOP sets the rule, the template records the evidence, and the how-to shows the steps.

## Finding an SOP

Every SOP in this folder is in the file list above, sorted by ID. The filename names the process it governs.

## When to use an SOP

- **Use an SOP** when you need to know what must happen at a stage, who is responsible, and what a gate requires.
- **Use a [template](../templates/)** when you need to record that a gate was passed.
- **Use a [how-to](../howto/)** when you need to complete a specific task, step by step.

## File naming

```
EDI-SOP-<NNN>_<Title>.pdf
```

| Part | Meaning |
|---|---|
| `EDI-SOP-<NNN>` | Permanent ID. Never reused. |
| `<Title>` | Short title, words joined by hyphens. |
| `.pdf` | All SOPs are published as PDF. |

Example:

- `EDI-SOP-001_Map-Development-SOP.pdf`

Filenames carry no version number, so links stay stable across updates.

## Versions

The current version is printed in the page footer, with the SOP ID and title, on every page. Each SOP also ends with a Revision History table listing its versions.

| Change | Meaning |
|---|---|
| `v<major>` | Process change: a stage, gate, role, or standard changed. |
| `.<minor>` | Clarification, correction, or layout change. The process itself is unchanged. |

The full change history is in the repository's commit log.

## How an SOP is structured

Every SOP has the same core:

- **Document control:** ID, title, version, owner, and approval.
- **Purpose and scope:** what the process is for and what it covers.
- **Roles (RACI):** who is responsible, accountable, consulted, and informed at each stage.
- **Procedure:** the stages or steps, each with entry and exit criteria.
- **Related templates:** the evidence each gate requires.
- **Revision History:** version, date, and a summary of each change.

The remaining sections depend on the process the SOP governs. A development SOP adds development and testing standards. An incident management SOP adds severity levels, escalation paths, and response targets. Where a process is measured, the SOP defines its quality metrics. New SOPs add whatever sections their process needs.

## SOPs and templates

The SOP sets the rules and the gates. The [templates](../templates/) are the evidence each gate requires. Each SOP lists its templates under "Related templates," and each template names the SOP stage it serves. Complete them per change and attach them to the change ticket. A gate without its completed template has not passed.

## Adapting an SOP

- Replace role names with your organization's titles. Keep the RACI assignments intact.
- Set your own metric targets. The values in each SOP are starting points.
- Map lifecycle stages to the statuses in your ticketing workflow.
- Link the how-to guides for tasks done within a stage, so people find the steps at the point of need.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE.md).

---

Back to the [repo overview](../README.md) · See the [templates](../templates/) for the evidence and the [how-to guides](../howto/) for the steps.
