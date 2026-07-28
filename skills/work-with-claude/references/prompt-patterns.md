# Claude Continuation Prompt Patterns

Use these as structures, not scripts. Replace every placeholder with verified task context. Remove irrelevant sections.

## User-feedback delta

```text
New user feedback. Treat this as a delta to the active task.

NEW RULE
<Quote or faithfully translate the feedback.>

REPORTING
Continue with <QUIET | STANDARD | DETAILED> reporting. This controls only communication, not creativity, reasoning, implementation depth, or tool use.

SUPERSEDES
<State the prior instruction that no longer applies. Use "nothing" when additive.>

UNCHANGED
<List the selected concept, invariants, boundaries, and pending verification that remain active.>

CREATIVE FREEDOM
<State open, directed, or constrained, and only where.>

ACTION
First acknowledge your interpretation and surface any product/design question. Then update the owning layer without unrelated changes and verify:
<acceptance evidence>.
```

Do not tell the user the delta was delivered until Claude acknowledges it.

## Queue acknowledgement

Use a concise user-facing update. Do not send this backlog item to Claude.

```text
Queued as <Q-id> at position <n>: <user outcome>.

Active: <Q-id and outcome>
Next: <ordered Q-ids and outcomes>
Waiting on you: <decision or none>

This item has not been sent to Claude. I will refresh its brief against the current code and dispatch it automatically after the active item reaches a verified checkpoint.
```

## Immediate active-item interruption

Interrupt only for an explicit now, stop, cancel, or replace instruction; a safety issue; or a correction that invalidates continued work.

```text
Stop the current task at the nearest safe boundary. New user instruction:

<Quote or faithfully translate the immediate instruction.>

THIS <SUPPLEMENTS | SUPERSEDES | CANCELS>:
<Exact active instruction affected.>

Before editing further, report:
1. what is already changed;
2. any command or mutation still in progress;
3. whether the worktree needs cleanup or verification;
4. your interpretation of the new instruction;
5. any user decision required.

Do not continue the superseded direction. Do not revert partial work unless I authorize it after reviewing your state report.
```

## Dispatch the next queued item

Use only after Codex has closed the prior checkpoint and marked this item active.

```text
The prior big-picture item has reached its verified checkpoint. Begin the following item as the only active big-picture task:

QUEUE ITEM
<Q-id>: <original user wording plus confirmed refinements>

CURRENT STATE
<Fresh repository, runtime, design-direction, and worktree evidence.>

CREATIVITY MODE
<Creative prototype sprint | Directed implementation | Constrained creativity | Technical repair>

DEPENDENCIES AND INVARIANTS
<Verified dependencies, preserved behavior, and boundaries.>

ACTION
Refresh the current owning layers rather than relying on assumptions from when this item was queued, then proceed directly into the mode's prototype or implementation outcome. Do not stop for plan approval. Stop only for a material unresolved decision, safety boundary, or verified contract conflict.

Do not start or infer any later queue item. The orchestrator will dispatch later work separately.
```

## Relay Claude's questions

Present unresolved questions without answering them:

```text
Claude needs your decision before continuing:

1. <Question>
   - Why it matters: <impact>
   - Options Claude identified: <options and tradeoffs>
   - Claude's recommendation, if any: <recommendation>

Codex's technical recommendation, if useful: <clearly labeled recommendation>
```

Send the user's answer back without adding an unrequested aesthetic decision.

## Evidence-based technical correction

```text
Independent technical review found a verified issue:

EVIDENCE
<Reproduction, file/line, screenshot, failing check, or contract.>

REQUIRED OUTCOME
<Correctness, security, accessibility, data, or selected-design contract that must hold.>

Keep the user's selected visual direction and your design ownership. Diagnose the root cause, implement the smallest correct fix, and rerun:
<stage-appropriate focused checks; broad final checks only when repository guidance or risk requires them>.

Do not treat subjective Codex taste as a requirement and do not expand scope.
```

## Named-session recovery

```text
Resume the existing task. Do not restart discovery or redo completed work.

Before acting, report:
1. what is complete;
2. what remains;
3. the user's selected direction and unresolved choices;
4. active safety/publication boundaries;
5. current server/browser state as you understand it;
6. the next single action.

Wait for confirmation if your account conflicts with this continuity note:
<Codex's concise verified state>.

Resume only the currently active item. The orchestrator owns any later queue and will dispatch it separately.
```

## Final engineer handoff

```text
Stop editing and provide a concise engineer handoff:

- implemented behavior and design direction;
- files and owning layers changed;
- design/animation skills used;
- tests and runtime checks with exact outcomes;
- unresolved questions or gaps;
- Git status, including untracked and staged files;
- prohibited actions you did not take.

Do not include a chronological transcript or progress narration. Keep the durable conversation available until the orchestrator finishes independent verification.
```
