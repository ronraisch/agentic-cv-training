# HTTP, SQL, services and application boundaries

[All training](index.md) · [Source coverage](sources.md)

## Saved. Crashed. Delivered again.

A worker saves its prediction, crashes before acknowledging, then receives the same job again. What stops a duplicate result?

![Saved. Crashed. Delivered again. Save output; Crash before ACK; Same job redelivered](assets/development-interfaces-toy.svg)

| Notice | Interpret | Check |
| --- | --- | --- |
| ACK first risks lost work | Save first permits retries | Stable IDs support idempotency |

<details>
<summary>Reveal the catch</summary>

Reliable systems plan for the gap between two operations, not only the happy path.

</details>

### In code: Replay one job ID

```python
outputs = {}

def save_once(job_id, prediction):
    return outputs.setdefault(job_id, prediction)

save_once("frame-7", {"cars": 1})
save_once("frame-7", {"cars": 1})  # Redelivery, same identity.
print(len(outputs))
```

**Expected output:**

```text
1
```

This single-process, in-memory toy illustrates stable identity only. A real worker also needs durable, atomic storage and a deliberate acknowledgement policy.

**Try it in 60 seconds:** Replay the same job ID twice and inspect durable output and consumer behaviour.

Read for understanding, not page completion. Skip what you can already explain.

<details>
<summary>Jump to a concept</summary>

- [Requests are explicit interfaces](#requests-are-explicit-interfaces)

- [SQL and persistent data](#sql-and-persistent-data)

- [Services, queues and state](#services-queues-and-state)

- [Research interfaces](#research-interfaces)

- [Learning path](#learning-path)

</details>

## Requests are explicit interfaces

HTTP connects clients and services through methods, paths, headers and bodies. A request to an inference endpoint needs a defined payload schema, encoding, maximum size and response/error schema. A connection timeout and a read timeout answer different questions. A successful TCP connection does not prove model readiness, and a 200 response does not prove the returned prediction belongs to the submitted image. Validate IDs, shapes and required fields at both ends.

A requests-style client sends data, checks status and parses the body. Do not retry every exception blindly: a timeout can occur after the service already committed work. Retrying then duplicates side effects unless a stable request identity supports idempotency. Authentication, serialization and schema evolution are separate from model quality. Logs should carry request/task IDs without exposing credentials or large sensitive inputs.

## SQL and persistent data

A relational table stores rows with declared columns and constraints. A primary key identifies a row; a foreign key expresses a relationship to another table. SELECT filters and projects rows; JOIN combines related tables; GROUP BY aggregates. A many-to-many join can multiply counts, so check cardinality before interpreting a metric. NULL represents missing/unknown information and has different comparison semantics from a normal value. Use parameterized queries rather than building SQL by concatenating untrusted input.

An index can accelerate selected access patterns but costs storage and write work. Query plans reveal what is actually scanned. A transaction groups operations that must succeed or fail together; isolation defines interactions with concurrent changes. Saving a prediction and marking a task complete in separate unprotected operations can leave contradictory state after a crash. Files and a broker may not share a single database transaction, so design recovery using stable IDs and explicit states.

## Services, queues and state

A service boundary should expose a meaningful operation with versioned inputs/outputs. Separate pure model prediction from transport and persistence so the same computation can be checked locally and through the actual consumer. A queue buffers jobs; a worker converts jobs into durable outputs. Define retryable errors, terminal errors and how partial results are recognized. A completed job is supported by a saved/reloaded artifact and a consumer check, not simply an in-memory flag.

## Research interfaces

A component contract includes data formats, units, label order, supported shapes and relevant numerical behavior. Keep experiment changes within authorized components and compare alternatives on the same held-out population. Preserve checkpoints/configurations and visual evidence for multiple runs so tradeoffs remain inspectable. A single “best” score can conceal better recall at a slightly larger compute cost or a severe failure on one camera.

## Learning path

The archived developer outline named HTTP/requests and SQL but left their exercises undefined. These explanations retain those topics without inventing an old assignment. The active SAM2 and RabbitMQ exercises provide concrete service boundaries. Ask the agent for a failure between saving an output and acknowledging its job; draw the possible states and implement a bounded recovery check. During the mentor discussion, show exactly which persisted record and response establish successful completion.
