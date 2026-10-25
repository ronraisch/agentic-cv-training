# Verification practice

Treat an agent answer, a comment and a passing test as claims with a specific scope. Read the
actual implementation and its callers, run an independent example, inspect persisted output,
and show which artifact the executed path loaded. Ask the agent for concrete evidence when its
summary is broader than the change or the test it actually ran.

For an assigned product change, discover who produces and consumes the affected data. Ask product
questions before treating a generated implementation plan as a specification. Trace a normal
request from input to the final consumer and verify that a peer can replay it without oral context.

Record uncertainty and distinguish execution from inference. Keep experiments bounded, inspect
the semantic diff and explain important lines without the agent. This page is a working method,
not a catalogue of issues in the repository.
