# Engineering concepts: read before the corresponding lab

## 1. Boundaries are decisions about change
A connector changes when its provider changes schema; transport changes when timeout/retry
policy changes; ranking changes when the scientific definition changes. Put these decisions in
separate modules. Do not add an inheritance hierarchy merely because several functions exist.
Start with functions; introduce a small Protocol when multiple interchangeable implementations
and a consumer actually need it. Composition lets tests supply a fake without patching globals.

In ResearchLab the shared HTTP client handles transient GET failures; a source adapter handles
pagination and schema; pipeline logic combines sources. A second retry decorator around a
connector multiplies attempts: three inner by three outer can make nine requests. A blanket
retry on POST may duplicate an operation. Retry only with explicit idempotency semantics.
A timeout is not evidence that the remote side did nothing. Concurrency must be bounded, preserve
identity even when completion order changes, and distinguish partial results from complete ones.

## 2. Contracts before implementation
A numerical signature is incomplete without shape, dtype, finite-value policy, mutation and device.
Define `normalize`: finite floating rank-2 input; new array; each nonzero row has unit L2 norm;
zero rows remain zero; invalid rank/integer/nonfinite input raises ValueError. Define ranking:
cosine similarity, nonzero finite matching query, integer 0 <= k <= N, deterministic ties retain
input order. Tests must check the input after the call, not just the output.
NumPy views can share storage: mutating a slice can change its parent. Broadcasting can silently
produce the wrong shape. Compare vectorized code against a small readable independent oracle.
Do not assert bitwise equality for arbitrary floating calculations; state a meaningful tolerance.

## 3. Data correctness is software correctness
A successful join is not proof that records were preserved. Duplicate keys create a many-to-many
Cartesian product. Validate uniqueness and cardinality, record missing IDs explicitly, and join
by identity rather than row order. Preserve provenance: source revision, query, preprocessing,
seed, package/model version and data fingerprint. Scene-related samples must stay in one split;
a random row split can leak a scene into both training and evaluation. Never fit preprocessing on
held-out data. Published metrics without split provenance are not reproducible evidence.

## 4. Inference is not training
`model.eval()` changes dropout/batchnorm behavior; `torch.inference_mode()` disables autograd
bookkeeping. Neither substitutes for the other. Move inputs to the documented device, bound batch
size, detach and move outputs to CPU before retention. Restore the caller's model mode if your
contract promises no mode changes. Seeding alone does not guarantee determinism across devices,
versions or nondeterministic kernels. Measure memory and numerical agreement on the real path.

## 5. Tests need an independent question
Unit: a zero vector. Integration: two HTTP pages through the adapter. End-to-end: CLI report.
Regression: a previously failing input. A mock copied from the implementation can encode the same
mistake. Use a provider contract and deliberately malformed responses. A test suite that passes
when a known defect is restored is weak for that defect. Coverage percentages do not answer this.

## 6. Maintain a public package
Keep import-time work cheap and free of network access. Package with pyproject and src layout;
install a wheel outside the checkout to catch accidental relative paths. Document public keys and
errors, use deprecation/versioning for breaking changes, and validate with a downstream consumer.
Pin application environments with a lock; keep library dependency constraints intentional. A
notebook is an exploration surface; reusable preprocessing belongs in tested modules. Document
why a decision exists and when to revisit it, rather than narrating every line.

## 7. Review behavior, not apparent sophistication
Ask: what real failure does each class, fallback, cache and generic helper prevent? Remove unused
frameworks. Broad exception catches can turn a service outage into an empty scientifically
plausible dataset. Caches need keys that include data/model/preprocessing revisions and an
invalidation policy. Prefer one small change whose consequences a peer can inspect. The human
accepting an agent patch still owns the result and its uncertainty.
