# How-To Guides

A how-to guide in this repo walks through one EDI task, start to finish. The SOP sets the rule, the template records the evidence, and the how-to shows the steps.

## Finding a guide

Guides are grouped into two folders by task type. Open a folder to see its guides, sorted by ID.

| Folder | Use it when |
|---|---|
| [troubleshooting/](troubleshooting/) | Something failed or doesn't reconcile, and you need to find out why: a rejected acknowledgment, a failed transmission, a missing document. |
| [development/](development/) | You are building or testing something: a map, a validation script, an automated test. |

Each guide's **Task type** field, in the header block on page 1, matches its folder.

Each guide covers a task that comes up often in production and is usually done from memory instead of from a written procedure.

## When to use a how-to

- **Use a how-to** when you need to complete a specific task: trace an acknowledgment, read an envelope, find why a file failed, test a map.
- **Use an [SOP](../sop/)** when you need to know what must happen at a stage and who signs off.
- **Use a [template](../templates/)** when you need to record that a gate was passed.

A how-to does not create a record and needs no sign-off. If a task produces evidence for a gate, the guide points to the template that captures it.

## File naming

```
EDI-HOWTO-<NN>_<Title>.pdf
```

| Part | Meaning |
|---|---|
| `EDI-HOWTO-<NN>` | Permanent ID. Numbered in one sequence across both folders. Never reused. |
| `<Title>` | Short task title, words joined by hyphens. Starts with a verb. |
| `.pdf` | All guides are published as PDF. |

Example:

- `troubleshooting/EDI-HOWTO-01_Match-997-to-Outbound-850.pdf`

Filenames carry no version number, and a guide stays in its folder once published, so links stay stable across updates.

## Versions

The current version is printed under the title on page 1. Each guide also ends with a Document History table listing its versions.

| Change | Meaning |
|---|---|
| `v<major>` | A step was added, removed, or changed, or the scope changed. |
| `.<minor>` | Clarification, correction, or layout change. The steps are unchanged. |

The full change history is in the repository's commit log.

## How a guide is structured

Every guide has the same sections, in the same order:

- **Header block:** the X12 versions or protocol it applies to, the transactions involved, the task type, and the estimated time.
- **Introduction:** what the task is and why you would do it.
- **Scope:** what the guide covers and what it does not.
- **Before You Start:** the access, files, and knowledge you need.
- **Example:** the sample file or scenario used in every step.
- **Steps:** numbered actions, one action per step, with the expected result where it matters.
- **Result:** what you have at the end of the task.
- **Appendix** (optional): reference tables such as error codes.
- **Need Help?:** where to report an issue or ask a question.
- **Document History:** version, date, and a summary of each change.

Guides stay short on purpose. Background theory belongs in a reference, not in a procedure.

## Adapting a guide

- Replace the synthetic partner IDs, qualifiers, and control numbers with your own when you build an internal version.
- Swap tool-specific steps for the translator, platform, or monitoring tool you use. The logic of the task stays the same.
- Replace the Need Help? section with the team that owns the task in your organization.
- Link the guide from the SOP stage or runbook where the task happens, so people find it at the point of need.

## Data and license

All data, partner IDs, and company names are synthetic. Licensed under [CC BY 4.0](../LICENSE.md).

---

Back to the [repo overview](../README.md) · See the [SOPs](../sop/) for the rules and the [templates](../templates/) for the evidence.
