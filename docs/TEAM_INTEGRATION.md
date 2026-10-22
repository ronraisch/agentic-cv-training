# Skills and MCPs used by your actual team

The course examples are not claims about your internal tools. Before the cohort starts, a mentor
fills `templates/team-tool-inventory.csv` with at least two real skills and two available MCP tools
(or explicitly marks an unavailable category). Record owner, triggers, permissions, inputs/outputs,
versions, offline fallback and a known evaluation task. Use approved synthetic/declassified data.

## Skill installation and practice
Example skills live in `.agents/skills/`. This is a portable course location, not a guarantee every
harness auto-discovers it. For each harness use its installed-version documentation to configure
project skills, or explicitly supply the SKILL.md path. Check the session trace for actual loading.
Do not copy the same instructions into several divergent directories. Do not install course skills
globally unless the team wants that behavior. The examples are committed project assets.

A skill has name/description frontmatter and a task-specific procedure. Its metadata helps decide
when to load it; references are loaded only when needed. Scripts can avoid repeated generation.
Evaluate both a task that should trigger it and one that should not. A persuasive SKILL.md is not
an evaluation. See lab 07 for required before/after runs and the negative case.

## MCP server connection
1. Install the pinned extra: `uv sync --extra dev --extra mcp --locked`.
2. Run `uv run python tools/check_mcp.py` to verify real initialization, discovery and tool calls.
3. Adapt `templates/mcp-config.example.json` to absolute paths and the client's supported config
   location/schema. The example is a common mcpServers shape, not a universal client config.
4. Connect the server in the approved coding client, discover `list_samples`, request one train
   record, then try an invalid limit. Inspect bounded results and failures. Record actual tool calls.
5. Stop/disconnect the server when finished. No TCP port, auth secret or real dataset is needed.

The pinned SDK uses stdio. stdout carries protocol messages; diagnostics belong on stderr.
The server exposes metadata only and no shell, arbitrary path or arbitrary URL tool. Adding a
capability requires a schema, bounds, failure semantics and tests. A tool description is model
context; it cannot enforce permissions. Enforce boundaries in server code and host configuration.

## Internal-tool onboarding gate
For EACH chosen internal skill/MCP: explain why it exists, run a successful case, trigger a failure,
inspect provenance and permissions, demonstrate the fallback, and teach a peer to use it.
If access is missing, mark the gate BLOCKED, run the example substitute and assign an access owner.
Do not mark internal-tool onboarding complete on the basis of our synthetic substitute.
