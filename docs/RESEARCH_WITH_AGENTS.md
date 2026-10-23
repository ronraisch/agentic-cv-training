# Learn research with an agent

Use the approved repository-aware agent to understand a problem, not only implement a ticket.
Reserve two hours each week within the syllabus. The individual teach-back itself is agent-free.

## A bounded research conversation

1. Spend 15 minutes stating the consumer question, assumptions, known code paths and unknowns.
2. Spend 30 minutes asking the agent to teach one missing concept, compare two plausible methods
   and expose where each assumption fails. Ask for a toy numerical/geometric example.
3. Spend 30 minutes checking a primary source, installed API or independently computed example.
   Separate what the source establishes from what it merely suggests for our data.
4. Spend 30 minutes designing/running the smallest experiment that could falsify the idea.
5. Spend 15 minutes writing a short research card and queuing at most two mentor questions.

If an experiment needs longer compute, keep the research card explicit about what remains untested.
Do not spend the entire slot collecting more explanations of the same idea.

## Repository-aware prompts

"Read these entrypoints and the task. Explain the consumer decision and the research assumptions
before suggesting code. Separate observed call paths, inferred requirements and missing evidence.
Give me two plausible approaches and one example where each fails. Ask me to predict a toy result."

"I think this preprocessing helps. Challenge the hypothesis. Which confounders or changes to the
measurement could produce a fake improvement? Design a paired comparison on grouped hold-out data."

"Teach me why this representation can answer a presence question but might fail on a temporal
event. Show a counterexample. Help me test whether my actual sampler preserves the needed evidence."

"Check my explanation against one primary source. Identify an unsupported claim rather than
rewriting it more confidently. Do not invent results, citations or private system behavior."

For product ambiguity, the mentor is the product owner; the agent may help discover questions but
cannot approve requirements. For literature review, model output is a lead, not a reference.
Use approved internal tools for internal code/data. Public ChatGPT can discuss sanitized toy
examples and general concepts; never paste restricted repository content into an unapproved service.

## Research card

Use templates/research-learning.md: question, explanation in your own words, alternatives,
source/version, observed evidence, counterexample, smallest experiment, current uncertainty and
next decision. One page is enough; a transcript dump is not the deliverable.

Minimum rhythm: one card a week, covering development/product reasoning, geometry, evaluation,
classical ML, cloud-model design and video/consumer tradeoffs over the six weeks. You may learn
from independent sources instead of the provided reading when you demonstrate the same outcome.
Record the substitution; do not add its time on top of the fixed study budget.
