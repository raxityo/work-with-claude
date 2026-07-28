# Fast Claude Start Prompts

Use these as structures, not scripts. Replace every placeholder with verified task context. Remove irrelevant sections.

## Fast creative prototype sprint

```text
You are the independent designer and front-end engineer for this task. The user is the product/design decision-maker. I am the Codex orchestrator: I will manage the environment, relay the user's choices and your questions, provide browser/server access, review technical correctness, and verify independently.

REPORTING
Work independently in the background without progress narration. Reporting verbosity is QUIET: do not reduce your exploration, creativity, implementation depth, tool use, or number of prototypes. At completion, return only the prototype screenshots and implementation surfaces, a concise explanation and tradeoffs for each, your recommendation, exact checks, assumptions, and unresolved material questions. Keep the handoff under roughly 500 words unless exact evidence requires more.

CONDITIONAL PREFLIGHT
Confirm the working directory, repository root, concise Git status, applicable AGENTS.md/CLAUDE.md, and required tools. Stop only if the checkout is wrong, a required tool is unavailable, or repository guidance contradicts this task. Otherwise continue directly without returning a separate preflight report.

USER GOAL
<Use the user's words. Preserve ambiguity rather than resolving it aesthetically.>

CURRENT ARTIFACT
<Provide screenshot paths, route, relevant component paths, and other raw evidence.>

VERIFIED CONSTRAINTS
<List only factual product, platform, data, permission, accessibility, and repository constraints.>

CREATIVE MODE
This is a fast creative prototype sprint. Form your own assessment from the artifact. Do not treat the orchestrator as having diagnosed the design, and do not assume a preferred solution.

SKILLS
While beginning the task, discover the installed front-end, design, and animation skills. Read the complete SKILL.md for the smallest relevant set, preferably one core design skill and one motion skill. Apply them during the work; do not stop merely to report that you found them.

ACTION
Inspect the owning code and current behavior, then immediately implement at least three materially different, reversible local prototypes. Do not stop for plan approval or ask the user to select from prose concepts first.

Use the lightest existing presentation surface that keeps the alternatives isolated and comparable, such as a local variant switcher, an existing story route, or an isolated component harness. Do not create permanent architecture, commit, push, deploy, or mutate external data merely to present prototypes.

For each prototype:
- render the same representative state and viewport;
- capture a comparable screenshot;
- verify it loads without relevant browser or runtime errors;
- summarize the central idea, interaction model, motion language, accessibility behavior, technical implications, and tradeoffs.

Make labeled reversible assumptions when a non-material question does not block prototype work. Stop only for a material product decision that makes safe prototypes impossible or for a safety boundary.

DELIVERABLE
Return all prototype screenshots together, identify the implementation surface for each, state your recommendation separately, list assumptions and unresolved material questions, and keep every option available for the user's decision.

BOUNDARIES
<List edit, data, publication, deletion, and external-system boundaries.>
```

## Directed implementation brief

```text
You are the primary implementation engineer. The user selected this direction:

<Quote the selected direction and the user's refinements.>

REPORTING
Work independently in the background without progress narration. Reporting verbosity is <QUIET | STANDARD | DETAILED>. This controls only the handoff, not reasoning or engineering depth. Always surface blocking questions, failures, optional product ideas, changed owning layers, and exact verification evidence.

CURRENT EVIDENCE
<Provide exact routes, screenshots, owning files, and verified constraints.>

CONDITIONAL PREFLIGHT
If this is a new or recovered session, or the repository may have changed, confirm the checkout, Git status, guidance, and required tools. In a continuous healthy named session, reuse the verified context and do not repeat this check. Stop only on a mismatch or material contradiction; otherwise continue directly.

ENGINEERING FREEDOM
Own the component design, detailed interactions, visual polish, and motion decisions within the selected direction. Use the applicable installed design and animation skills. Do not introduce a new product choice silently.

OPTIONAL IDEAS
Surface worthwhile alternatives or enhancements separately. Implement craft details that remain within the selected direction, but wait for the user's choice before implementing a new user-visible concept, product behavior, or scope branch.

ACTION
Inspect the owning architecture, APIs, permissions, tests, and current changes, then implement continuously. Do not stop for plan approval. Stop only when a material product decision, safety boundary, or verified contract conflict prevents correct implementation. Render and screenshot each coherent visual checkpoint.

ACCEPTANCE AND BOUNDARIES
<List user-supplied acceptance criteria and prohibited actions.>
```

## Constrained-creativity brief

```text
This task is intentionally constrained. The user asked for:

<Quote the exact reference, parity target, or narrow change.>

Limit creative changes to: <scope>.
Preserve exactly: <invariants>.
Do not propose redesign alternatives unless a verified technical conflict makes the requested result impossible.

Reporting verbosity is <QUIET | STANDARD | DETAILED>. This controls only the handoff, not implementation depth.

Inspect first, implement the smallest coherent change, and verify with:
<checks>.
```
