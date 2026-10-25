# Engineering references

Use small, explicit interfaces around operations that change for different reasons. Read current
callers before adding abstractions. State input/output meaning, shape, dtype, units, identity,
error semantics and persistence. Keep transport policy separate from provider-specific parsing.

A repository claim needs an executed example and a consumer check. Tests answer bounded questions;
compare meaningful behavior with independent expectations rather than reproducing an implementation.
Inspect the saved artifact and fresh-load behavior before reporting a completed training/inference
change. Read [verification practice](PITFALLS.md) and the assigned local lesson for concepts.

Use [the working baseline](BASELINE.md), [data contracts](DATA_FORMATS.md) and
[offline setup](OFFLINE_SETUP.md) to run the system. Existing callers and actual executed settings
are the source of evidence when a secondary note and runtime behavior disagree.
