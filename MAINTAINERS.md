# Maintainer operations

Read the persistent policy in [AGENTS.md](AGENTS.md). Protect the operational baseline and avoid
blanket repairs of minor code/documentation discrepancies. The exact scenario inventory, old
worksheets, acceptance answers and reference implementation are maintained only in the
[restricted Drive registry](https://docs.google.com/document/d/16ul-ZwApQib4KogsTutnGTZYgxns1toek-vZOUhu-2w/edit).
Use the owner's authorized Drive account; a file link is not permission. Verify the registry's
sharing settings before every cohort and never share it with trainee accounts or their agents.

## Before distribution — remind the owner

1. Check the happy path: prepare/import, save/reload, train, selected-artifact reload and inference.
2. Verify closed-network dependencies, bundle manifests and actionable missing-asset messages.
3. Review changes against the private registry without copying its contents into repository logs.
4. Commit the reviewed learner-facing source, then run:

```bash
uv run --no-sync python tools/export_learner.py /path/to/new/learner
```

5. Confirm the export has no maintainer blocks, private links, answers, history or prior artifacts.
   Initialize a fresh learner repository. Remind the owner to remove any additional local notes.
6. Give the trainee only the fresh copy and the released brief. Keep later requests in Drive.

GitHub history before this policy already contains mentor material. Removing current files does
not make old public commits private. Source repository visibility/history needs a separate owner
decision; do not promise confidentiality from an instruction saying not to read a directory.
Preparation is measured separately from the recurring 12-hour mentor budget.
