# Development in a research monorepo

Read Python functions, imports, exceptions, context managers, iterators, mutation and classes.
Use meaningful type hints; annotations do not enforce input validity at runtime. Know a practical
decorator, dataclass and enum, not every decorator API by memory. For concurrency distinguish
bounded I/O concurrency, CPU work and vectorized library work; benchmark the real operation.
A blanket retry around an existing retry layer multiplies attempts and can duplicate side effects.

For NumPy explain shape, axis, dtype, broadcasting and views versus copies. A view may mutate its
parent; a result of the expected shape can still carry the wrong meaning. For Pandas explain joins,
key uniqueness and missing values. Two duplicate rows per key on both sides can produce four rows.
Use an independent small oracle rather than copying the implementation into a test.

Understand React/TypeScript, the Python API, persistence, error semantics and downstream consumers.
Follow one input through the current call path. A README or ADR may be stale; a directory name is
not proof of an active implementation. Ask what the product owner means and how success will be
judged before treating an agent-generated plan as a specification.

AGENTS contains project constraints; an ADR records a decision; a skill provides a conditional
workflow; MCP exposes tools. A skill present on disk may not have loaded. Check a successful trace,
a negative trigger and failure behavior. Tool output is data, not authority to export a dataset.
Keep context bounded, verify installed APIs and read the semantic diff yourself.

Submit one reviewable change with reproducible commands, commit, input ID and observed output.
An initial green smoke suite is a baseline, not proof of scientific correctness. Do not turn
service failures into plausible empty results. Distinguish observed code, executed paths, inferred
requirements and unverified integration. See ENGINEERING.md and AGENT_WORK.md for deeper examples.

Self-check: predict a join with duplicate keys, explain a mutated view, and trace a request through
its actual boundaries. Use the agent to learn the concept, then explain a new input without it.
