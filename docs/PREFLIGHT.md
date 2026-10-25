# Local smoke and readiness-record preflight

Run this with the project's approved interpreter after the
[locked installation](GETTING_STARTED_INTERNAL.md#python-and-uv-through-artifactory).
It does not install packages, download data/weights, call internal endpoints or execute commands
from a configuration file. It preserves the intentional application defects.

## Starter checks

From the checkout:

```bash
uv run --no-sync python tools/preflight.py --scope starter
```

The command runs the synthetic ResearchLab CLI with explicit fixture paths, validates its report
schema, checks the two course skill files and runs the real local stdio MCP success/error probe.
It uses the current Python interpreter and resolves repository paths from the script, so an
absolute invocation also works from another directory or a history-free learner export.
It does not run pytest recursively; continue to run `uv run --no-sync pytest` separately.

`PASS` means those three local checks ran. It does not establish correct research algorithms,
client skill activation, an installed research stack or working internal inference. The expected
MCP invalid-input traceback is captured; unexpected command failures remain failures. A missing
package is `BLOCKED`, with the approved environment as the next action. For detailed failure
logs, replay the fixed command shown in the JSON report.

## Internal handoff records

The default scope is `handoff`: starter checks plus the coarse components in
[the readiness template](../templates/readiness.csv). The public template is intentionally
incomplete, so this invocation should exit **2**, not indicate a ready cohort:

```bash
uv run --no-sync python tools/preflight.py
```

Inside the approved network, the supplying owner fills an internal copy of that CSV, then runs:

```bash
uv run --no-sync python tools/preflight.py --readiness /approved/internal/readiness.csv --output artifacts/preflight.json
```

For each required runtime component, the tool requires status `VERIFIED`, a non-placeholder owner,
a revision or checksum reference and a nonempty local file named by `smoke_evidence`. Relative
evidence paths resolve beside the CSV. Use a sanitized transcript of an executed smoke as evidence.
The component IDs come from the template; historical source-reading rows are informational and
do not replace runtime checks. Missing components block; duplicate IDs/columns and malformed CSV
fail. URLs and shell commands are not fetched or executed as evidence.

Such records receive **RECORDED**, never `PASS`: the tool checks metadata/file presence, not
transcript contents, authenticity, freshness, asset hashes, label quality or live system behavior.
It cannot replace the per-asset preparation checklist, actual data decode/model/service checks
or mentor acceptance. All reports explicitly keep internal integration `UNVERIFIED`. The supplying
owner remains responsible for executing and reviewing the actual checks in the trainee's pod.
The [research-environment handoff](RESEARCH_ENVIRONMENT.md) describes those capabilities.

## Output and exit status

Add `--json` for structured stdout; `--output` saves the same report as JSON. Output includes the
scope, interpreter, timestamp, source commit/dirty flag when available, per-check status and
missing-record owners. A history-free export has null Git fields; retain the exporter command's
source commit alongside its evidence. Child stdout/stderr and evidence-file contents are not
included. Keep internal reports local; manually sanitize any evidence approved for publication.

| Exit | Meaning |
|---|---|
| 0 | Starter smokes passed; in handoff scope the required records are present as `RECORDED` |
| 1 | A local smoke failed, timed out or returned an invalid report; or the CSV is malformed |
| 2 | Required packages/records/evidence are blocked, or CLI arguments/output are invalid |

A failure takes priority over a block. A recorded handoff is not a verified deployment.
