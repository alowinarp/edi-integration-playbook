# EDI Integration Playbook

**A practitioner's field guide to building, onboarding, and running EDI integrations**

Most EDI documentation explains what a segment *is*. This playbook explains what to *do*: how to develop maps to a repeatable standard, how to test and release them without surprises, and how to find out why a file failed when the tooling won't tell you.

---

## Why this exists

EDI translators are good at syntax validation. They are not good at telling you *why* a file died.

A pattern I've seen repeatedly in production: when an inbound interchange's envelope values don't match any configured trading partner profile, the translator rejects the file outright — **no 997, no error report to the sender.** Someone has to pull the raw file, compare ISA/GS values against the partner profile by hand, find the mismatched qualifier or ID, and explain to the business what failed.

That pattern — *valid enough to arrive, wrong enough to fail, invisible to the tooling* — repeats across envelopes, acknowledgments, and business-rule data. This playbook documents the procedures, checks, and templates that close those gaps.

---

## Who it's for

- **EDI analysts and developers** who want repeatable procedures, not tribal knowledge
- **Integration leads** standardizing development, testing, and go-live across many partners
- **Data and analytics engineers** who inherit EDI-fed pipelines and need to understand the source
- **Business stakeholders** who need to know why an order, ASN, or invoice didn't land

---

## What's inside

```
edi-integration-playbook/
├── README.md        This overview
├── sop/             Standard operating procedures
├── templates/       Stage templates and checklists
├── how-to/          Task-level guides
└── LICENSE.md
```

| Folder | Contains | Use it to |
|---|---|---|
| `sop/` | Standard operating procedures: lifecycles, standards, roles, and quality gates | Set the rules your team works to |
| `templates/` | Forms and checklists that implement the SOPs, completed per change and attached to the change ticket | Produce the evidence each gate requires |
| `how-to/` | Task-level guides for specific problems: diagnosing failures, testing maps, onboarding partners | Get a specific job done, step by step |

Each folder has its own README listing its documents and how they connect. SOPs are published as PDFs. Templates are editable Word and Excel files, each with a PDF preview. All documents are versioned in the filename (for example, `_v1.0`).

---

## Principles

- **Vendor-neutral.** Procedures apply to any translator or mapping tool and to X12, EDIFACT, XML, JSON, and flat-file formats.
- **Practical over theoretical.** Every document answers "what do I do next?", not "what does this segment mean?"
- **Evidence-based gates.** Every stage ends with a recorded result, not a verbal "looks fine."

---

## Data and confidentiality

All sample files, partner IDs, company names, and scenarios are **synthetic**. No production data, real trading partner identifiers, or employer-confidential material is included.

---

## Feedback

Spotted an error, or have an EDI failure pattern worth documenting? Open an issue.

## License

Documents are licensed under [CC BY 4.0](LICENSE.md). You may use and adapt them, including commercially, with attribution.

---

**Author:** alowinarp — EDI/B2B integration specialist (retail supply chain, healthcare)

Available for EDI documentation, standards, and integration work. Contact via [GitHub](https://github.com/alowinarp).
