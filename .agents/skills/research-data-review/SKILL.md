---
name: research-data-review
description: Review research data adapters and pipeline changes. Use when editing connectors, joins, pagination, schema validation, or split logic.
---

Read the task contract and relevant diff. Locate the existing HTTPClient before proposing a new transport. Check identity, cardinality, completeness, scene split and provenance. Require a malformed-input case and a service-failure case; use local fixtures. For the detailed checklist load [references/checks.md](references/checks.md). Report findings by consequence with code locations and a reproducer. Distinguish observed failures from hypotheses. Do not expand task scope or silently repair unrelated defects.
