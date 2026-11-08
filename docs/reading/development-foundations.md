# Linux, Git, containers and Python foundations

[All training](index.md) · [Source coverage](sources.md)

## When the same code runs in a different environment

The shape parser runs correctly from VS Code. Inside the container, it fails to find its input. Nothing in the parser changed: `./data` now refers to a different directory, and the file may not be mounted there at all.

![It works on my pod. Why not yours? VS Code: ./data; Container: /app; Missing mount](assets/development-foundations-toy.svg)

This is an easy failure to misdiagnose as a Python problem. The program depends on more than its source files: its working directory, interpreter, packages and mounted data all affect what it does. Reproducing the run means making those dependencies explicit.

Following one input from the terminal into the container gives the Linux, Git and environment concepts below a concrete purpose.

<details>
<summary>Jump to a concept</summary>

- [From an experiment to a reproducible program](#from-an-experiment-to-a-reproducible-program)

- [Linux and process boundaries](#linux-and-process-boundaries)

- [Git as an experiment record](#git-as-an-experiment-record)

- [Python execution and program design](#python-execution-and-program-design)

- [Environments, Docker and deployment](#environments-docker-and-deployment)

- [Following the shape parser through a real run](#following-the-shape-parser-through-a-real-run)

</details>

## From an experiment to a reproducible program

A research result depends on code, inputs, configuration and execution environment. A notebook output without these cannot establish which experiment produced it. Begin by locating the working directory, interpreter, imported package and input path. Relative paths resolve from the process working directory, not necessarily from the script's directory. A script that works only because an IDE silently changes that directory has an undeclared dependency.

## Linux and process boundaries

A filesystem contains directories and files addressed by absolute or relative paths. Learn to inspect and navigate with `pwd`, `ls`, `cd`, `cat` and a text search tool. Standard input, standard output and standard error are distinct streams. A pipe connects output to the next process's input; redirection writes a stream to a file. Check exit status as well as printed text: a program can print a warning and exit successfully or print nothing and fail. Permissions control reading, writing and execution. Environment variables are inherited by child processes and are strings, so configuration needs parsing and validation.

A process has its own address space; a terminal is just one way to interact with it. A tmux or screen session lets a long-running terminal task survive a disconnected client, but does not make the task restart after a machine failure. Know how to inspect processes, interrupt a job, read logs and distinguish a running process from a completed result. Avoid treating missing output as evidence of success.

## Git as an experiment record

A commit records a tree of tracked files plus metadata and parent history. The working tree contains your current files; the staging area selects the next commit. A branch is a movable reference to a commit; HEAD identifies the current checkout. Inspect `git status` and `git diff` before staging, and inspect the staged diff before committing. A local commit is not yet a remote backup. Fetch updates your view of the remote; merging combines histories and may require resolving conflicting edits. Resolve a conflict by understanding the intended behavior on both sides, then rerun the relevant example.

Use small feature branches and reviewable merge requests for exercises. Keep datasets, checkpoints, generated environments and credentials out of source history. Record their locations and checksums separately. To reproduce a result, check out the commit and load the matching configuration and model artifact, rather than assuming the current branch is equivalent.

## Python execution and program design

Python executes code through an interpreter and normally compiles source to bytecode internally. Dynamic typing means names refer to objects whose types are known at runtime. Assignment binds a name; it does not copy an object. If two variables refer to one list, mutation through either is visible through both. Prefer explicit inputs and return values to hidden mutable global state. Functions isolate behavior; modules organize related behavior; classes combine state with operations when an object's lifecycle matters.

Use exceptions for failed operations with useful context. A broad exception handler that returns an empty list can turn a failed image read into an apparently valid negative prediction. Validate file formats, coordinate systems and required fields at the boundary. Context managers close files even on exceptions. Iterators and generators support streaming, avoiding a full in-memory list when handling large data. Write docstrings for assumptions that types cannot express, such as units, array layout or whether a box endpoint is inclusive.

## Environments, Docker and deployment

A virtual environment isolates Python packages. Pip installs packages; uv manages environments and resolved dependencies. Conda is another environment/package system that appeared in the legacy material; this project's supported route is uv. Select the actual pod interpreter in VS Code and inspect where imports come from. A lockfile makes dependency selection repeatable; it does not include datasets or pretrained weights.

A Docker image is a layered filesystem and execution specification. A container is an instance with its own running processes and writable layer. Mount persistent data explicitly: deleting a container can remove unmounted results.

Build context determines what a Dockerfile can copy. A published port and a process listening on the expected interface are both needed for access. Compose describes connected services for local work; an OpenShift Deployment manages replicas, a Service provides an internal address and a Route exposes the chosen service. Check readiness, requests, logs and a real response instead of equating an accepted manifest with a working deployment.

## Following the shape parser through a real run

The shape-rendering capstone provides a small version of the same problem: a file is parsed, validated, turned into geometry and rendered. Running a new valid input and a malformed input reveals whether those responsibilities are actually separated. The later SAM2 service adds a container and network boundary around similar application logic. The assignments retain their manual-work requirements; understanding the path is the common thread.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html)

- [https://docs.python-guide.org/writing/style/](https://docs.python-guide.org/writing/style/)

- [https://docs.python.org/3/library/xml.etree.elementtree.html](https://docs.python.org/3/library/xml.etree.elementtree.html)

- [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)

- [https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)

- [https://www.katacoda.com/courses/docker](https://www.katacoda.com/courses/docker)

- [https://www.tutorialspoint.com/python/index.htm](https://www.tutorialspoint.com/python/index.htm)

- [https://www.tutorialspoint.com/unix/index.htm](https://www.tutorialspoint.com/unix/index.htm)

</details>
