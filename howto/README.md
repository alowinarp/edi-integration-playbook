# How-To Guides

A how-to guide in this repo walks through one EDI task, start to finish. The SOP sets the rule, the template records the evidence, and the how-to shows the steps.

## Finding a guide

Every guide in this folder is in the file list above, sorted by ID. The filename names the task, so you can scan the list for what you need to do.

Each guide covers a task that comes up often in production and is usually done from memory instead of from a written procedure.

## When to use a how-to

- **Use a how-to** when you need to complete a specific task: trace an acknowledgment, read an envelope, find why a file failed.
- **Use an [SOP](../sop/)** when you need to know what must happen at a stage and who signs off.
- **Use a [template](../templates/)** when you need to record that a gate was passed.

A how-to does not create a record and needs no sign-off. If a task produces evidence for a gate, the guide points to the template that captures it.

## File naming

```
HOWTO-<NN>_<Title>.pdf
```

| Part | Meaning |
|---|---|
| `HOWTO-<NN>` | Permanent ID. Never reused. |
| `<Title>` | Short task title, words joined by hyphens. Starts with a verb. |
| `.pdf` | All guides are published as PDF. |

Example:

- `HOWTO-01_Match-997-to-Outbound-850.pdf`

Filenames carry no version number, so links stay stable across updates.

## Versions

The current version is printed in the page footer, with the guide ID and title, on every page. Each guide also ends with a Document History table listing its versions.

| Change | Meaning |
|---|---|
| `v<major>` | A step was added, removed, or changed, or the scope changed. |
| `.<minor>` | Clarification, correction, or layout change. The steps are unchanged. |

The full change history is in the repository's commit log.

## How a guide is structured

Every guide has the same sections, in the same order:

- **Purpose / Overview:** what the task is and why you would do it.
- **Scope:** what the guide covers and what it does not. Transaction sets, directions, and versions are named here.
- **Prerequisites:** the access, files, and knowledge you need before you start.
- **Steps:** numbered actions, one action per step, with the expected result where it matters.
- **For questions, contact:** the role that owns the task.
- **Document History:** version, date, and a summary of each change.

Guides stay short on purpose. Background theory belongs in a reference, not in a procedure.

## Adapting a guide

- Replace the synthetic partner IDs, qualifiers, and control numbers with your own when you build an internal version.
- Swap tool-specific steps for the translator or monitoring tool you use. The logic of the task stays the same.
- Change the "For questions, contact" role to the team that owns the task in your organization.
- Link the guide from the SOP stage or runbook where the task happens, so people find it at the point of need.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE.md).

---

Back to the [repo overview](../README.md) · See the [SOPs](../sop/) for the rules and the [templates](../templates/) for the evidence.
