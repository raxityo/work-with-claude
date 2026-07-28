---
name: work-with-claude
description: "Orchestrate a persistent Claude Code CLI conversation as an independent designer and implementation engineer while Codex owns user communication, safety boundaries, an ordered work queue, and independent verification. Default to fast, background-first iteration: let Claude edit immediately, avoid streaming its transcript into Codex, monitor only compact status, create and render multiple UI prototypes before asking the user to choose, and dispatch one big-picture item at a time. Use when the user asks Codex to work or talk with Claude, run Claude in the background, minimize orchestration tokens, relay narrated feedback, queue later work, delegate repository tasks, explore UI or redesign directions, or resume and supervise a named Claude session. Preserve Claude's creative independence and route material subjective choices and product questions back to the user."
---

# Work With Claude

Use Claude as the active designer and engineer. Optimize for the shortest safe path to working artifacts and screenshots with minimal transcript ingestion by Codex. Keep Codex in the orchestrator role: establish only the environment Claude needs, translate the user's intent without taking ownership of it, relay decisions, protect boundaries, and verify the result independently.

Read [references/fast-start-prompts.md](references/fast-start-prompts.md) before composing the first Claude brief or transitioning from prototypes to a selected direction. Read [references/prompt-patterns.md](references/prompt-patterns.md) only before a material feedback delta, queue interruption or dispatch, technical correction, or recovery prompt.

## Keep the roles separate

- Treat the user as the product and design decision-maker.
- Treat Claude as an independent designer and engineer with room to inspect, propose, question, and implement.
- Treat Codex as the session, environment, communication, review, and verification owner.
- Do not make aesthetic or product choices for the user.
- Do not silently narrow Claude's creativity, choose among Claude's concepts, or turn a broad outcome into a prescribed design.
- Do not take implementation work away from Claude while Claude is the designated engineer. Read, inspect, challenge, run the environment, and verify independently; send implementation corrections back to Claude.
- Separate Claude-reported results from Codex-verified evidence.

## Default to fast iteration

Use fast iteration unless the user explicitly asks for a read-only review, planning-only work, or a slower approval process. Do not ask the user to opt into speed.

- Start Claude after a minimal repository and safety preflight. Do not duplicate Claude's design or code investigation before launch.
- Combine environment confirmation with the real task. Do not spend a separate Claude turn on a smoke test when the session can verify its context and continue.
- Let Claude make reversible local edits immediately. Do not require a plan approval before ordinary implementation.
- For open-ended UI work, require at least three materially different, rendered prototypes and a comparable screenshot of each before asking the user to choose.
- Let Claude select the lightest existing prototype surface: a local variant switcher, Storybook/story route, isolated component harness, or another reversible approach. Do not introduce permanent architecture merely to present alternatives.
- Keep all options available until the user chooses. Present Claude's recommendation without letting Codex select or discard a direction.
- Pause only for a material product choice that blocks safe progress, a destructive or external mutation, a security or data-integrity risk, or a contradiction with repository requirements.
- Use proportionate checks during iteration. Reserve broad validation for a coherent checkpoint, final handoff, or release boundary.

If three implemented variants would be disproportionately expensive or unsafe, ask Claude to produce the closest renderable alternatives available and explain the constraint. Do not silently fall back to lengthy prose concepts.

## Choose the task mode

Determine the mode from the user's request. State the mode to Claude.

| Mode | Use | Claude's first deliverable |
|---|---|---|
| Creative prototype sprint | Default for new UI, redesigns, visual systems, interactions, or open-ended front-end work | Inspect, implement, render, and screenshot at least three distinct prototypes in one continuous run; then provide questions and a recommendation |
| Directed implementation | Use after the user selects a prototype or supplies a sufficiently exact design and behavior | Inspect and implement continuously; stop only for a material unresolved decision or safety boundary |
| Constrained creativity | Use only when the user asks for minimal creativity, exact parity, a narrow patch, or strict adherence to a reference | Implement the smallest compliant result without unsolicited alternatives |
| Technical repair | Use for a reproduced bug, security issue, data-integrity issue, or acceptance failure | Diagnose, implement the smallest correct fix, and run the focused checks required by the risk |

Do not infer constrained creativity from a detailed repository or verification brief. Constrain only the aspects the user constrained.

## Preserve creative independence

For a creative prototype sprint:

1. Give Claude the current artifact: screenshots, route, relevant code, product context, and the user's words.
2. Do not provide Codex's critique, suspected design problems, preferred solution, or ranked ideas unless the user asked Codex to do so.
3. Distinguish objective constraints from opinions. Include permissions, data contracts, supported platforms, accessibility requirements, and existing product semantics without framing them as aesthetic defects.
4. Ask Claude to inspect the artifact, form its own diagnosis, and continue directly into reversible local implementation.
5. Require at least three genuinely distinct prototypes, not color or spacing variations of one idea.
6. Ask Claude to render each prototype at the same representative viewport, capture a screenshot, and summarize its visual hierarchy, interaction model, motion language, accessibility, technical implications, and tradeoffs.
7. Ask Claude to identify its recommendation and explain why, but present every prototype and the recommendation to the user without choosing.
8. Ask the user to select or refine a direction only after the prototypes and screenshots exist.

After the user selects a direction, let Claude own component structure, detailed interactions, visual polish, and motion decisions within that direction and the repository's constraints.

## Use design and animation skills

For front-end, design, or motion work:

1. Ask Claude to discover the installed project and user skills while beginning the task, not as a separate reporting gate.
2. Ask Claude to read the complete `SKILL.md` for the smallest relevant set of design and animation skills. Prefer one core design skill and one motion skill unless the task genuinely needs more.
3. Prefer applicable skills such as `emil-design-eng`, `animation-vocabulary`, `apple-design`, `find-animation-opportunities`, `improve-animations`, and `review-animations` when available and relevant.
4. Do not claim a skill is available until Claude verifies it.
5. Tell Claude to apply those skills during prototype creation rather than stopping merely to list or summarize them.
6. Require motion to respect reduced-motion preferences, input modality, performance, and accessibility. Do not add animation merely to demonstrate a skill.

If the user explicitly limits creativity or motion, pass that limit through exactly.

## Run a minimal preflight

Before launching Claude:

1. Read repository guidance. Read owning files only when needed to locate the correct checkout or establish a safety boundary; let Claude perform the primary task investigation.
2. Resolve the exact repository root, checkout or worktree, branch state, and current changes.
3. Record the user's boundaries: allowed edits, prohibited actions, external systems, real-data mutations, commits, pushes, deployments, and deletions.
4. Let Claude own the dev server and browser when they already work in its environment. Codex owns access setup, approvals, recovery, and independent final verification.
5. Verify Claude's executable, version, `--bg`, and `claude agents --json` support only on first use in the current environment or when a command fails or changes. Do not rerun help commands for every task.
6. Create a stable, unique session name from the repository and task, such as `project-ui-prototypes`. Keep that name for the entire task.
7. Pass model or effort arguments only when the user explicitly requests an override. Otherwise omit them and inherit Claude's configured defaults. Do not enumerate models before ordinary launches.
8. Prefer `--permission-mode auto` for trusted, reversible local work when the installed Claude version, account, repository policy, and user boundaries allow it. Otherwise use `--permission-mode acceptEdits` and pre-approve only the focused commands needed by the task. Never use `bypassPermissions`.
9. Add `--chrome` only when browser work is required and the integration is available.
10. Inherit Remote Control when the user's Claude configuration already enables it. Do not require or add a Remote Control argument merely for orchestration.
11. If this host is already known to block Claude's normal local state access, request the same narrowly scoped host permission at launch instead of deliberately failing once.

Launch the real task as a supervised background agent in the exact repository root. Pass the full brief as the initial prompt using the terminal tool's safe argument mechanism:

```bash
claude --bg --permission-mode auto --name <session-name> [--chrome] "<full-task-brief>"
```

Capture both the returned short agent ID and the durable session ID from `claude agents --json --all`. Treat the background supervisor and persisted conversation as durable state. Do not attach merely to watch Claude work.

Fall back to an interactive named PTY only when background agents are unavailable, repository policy prohibits them, or the task genuinely requires continuous synchronous pairing. Use only flags verified on that installed version. Preserve the reporting contract, poll at a coarse cadence with tightly bounded output, and disclose that transcript-free monitoring and automatic same-task wakeups are unavailable in fallback mode.

## Start the real task immediately

1. Complete one-time authentication, workspace trust, or Chrome integration confirmation before background dispatch when the current environment still requires it.
2. Put the full task in the initial background prompt. Begin it with a conditional preflight: verify the working directory, repository root, Git status, guidance files, and required tools; stop only on a mismatch or unavailable tool, otherwise continue directly.
3. Do not require Claude to report the preflight and return to the prompt before working.
4. If the launch reports a local-state permission failure, stop the unusable process, restart it with the narrowly scoped host permission required for Claude's normal state files, and resend the same active task through the named session.
5. End Codex's user-visible turn after recording the background ID, queue state, and monitoring path. Do not keep a Codex turn active to stream Claude's output.

## Brief Claude without over-directing it

Include:

- the role contract;
- the user's goal and language;
- verified artifacts and factual repository constraints;
- the selected creativity mode;
- relevant design and animation skill instructions;
- in-scope and out-of-scope work;
- explicit safety and publication boundaries;
- the required prototype or implementation outcome;
- acceptance criteria the user actually supplied;
- server, browser, and verification ownership;
- a request to surface material questions rather than assume answers.

For a creative prototype sprint, show what exists and ask Claude to assess it, implement three reversible alternatives, render them, and return comparable screenshots in one continuous run. Do not tell Claude what is wrong unless the user supplied that diagnosis.

For directed implementation, ask Claude to inspect the owning architecture and implement the smallest coherent solution without stopping for plan approval. Require a stop only when a material user decision or safety boundary remains unresolved.

## Control reporting verbosity

Treat reporting verbosity as an output contract, never as a creativity, reasoning, implementation, or tool-use limit.

| Level | Use | Claude handoff |
|---|---|---|
| Quiet | Default | No progress narration. Return only completion or blocking status, screenshots or artifact paths, changed owning layers, exact checks, unresolved questions, and recommendation. |
| Standard | When the user wants some explanation | Add concise rationale and tradeoffs without a chronological transcript. |
| Detailed | Only when the user asks | Include implementation reasoning, alternatives considered, and fuller verification context. |

Put the chosen level in the initial brief and every material continuation. For quiet mode, ask Claude to keep the final handoff under roughly 500 words unless exact errors, questions, or evidence require more. Do not suppress material product questions, optional design ideas, safety issues, failures, screenshot paths, or verification results.

Do not invent or depend on a `--quiet` flag. Claude's `viewMode: "focus"` changes terminal presentation, not the reporting contract or reliable model-token usage. Do not override the user's output style by default, and never pass `--verbose` except for targeted debugging.

## Relay questions and decisions

- Ask Claude to research factual repository questions itself.
- Relay every material unresolved product, visual, interaction, business, or preference question to the user.
- Do not answer those questions from Codex's taste or assumptions.
- Present Claude's options, tradeoffs, and recommendation faithfully.
- Relay material optional ideas Claude volunteers even when Codex prefers another direction. Do not suppress, merge away, or authorize them on the user's behalf.
- Let Claude decide craft and implementation details that stay within the selected direction. Treat a new user-visible concept, product behavior, or scope branch as a user decision.
- Add a Codex recommendation only when useful, label it as Codex's recommendation, and wait for the user to decide.
- Answer purely factual environment questions only after verifying the answer.
- Pause Claude when a new choice could cause destructive behavior, change product semantics, expand scope materially, or invalidate work in progress.
- When a question does not block reversible prototype work, ask Claude to make a labeled temporary assumption, continue, and surface the assumption with the screenshots.

## Maintain the orchestration loop

1. Do not poll or ingest the live transcript while Claude is working.
2. Check only the target agent's compact state. Prefer:

```bash
python3 <skill-dir>/scripts/claude_agent_status.py <agent-id-or-session-id>
```

Fall back to `claude agents --json --all` and select the exact ID. Never identify a session by name alone when duplicate names exist.
3. When the host supports in-task scheduled follow-ups, create one temporary heartbeat that returns to the current Codex task, checks only compact state about every two minutes, stays silent while state is unchanged, and cancels itself after `done`, `blocked`, `idle`, `failed`, or `stopped`. Re-arm it after replying to a blocked or idle session. This is status polling, not an exact completion callback.
4. Do not call `claude logs` while state is `working`. Read recent logs once when the state needs attention or is terminal.
5. If scheduled follow-ups are unavailable, leave Claude running and end the Codex turn with the exact session ID. Resume monitoring only when the user returns or another supported notification wakes the task.
6. Do not install a hook, daemon, plugin, or app-server bridge merely to simulate event-driven wakeup. A skill alone cannot guarantee an exact Claude-completion callback into the same Codex task.
7. Attach with `claude attach <agent-id>` only to answer a blocking question, deliver an explicit immediate steer, inspect a failure that compact status cannot explain, or continue the completed conversation. Detach it back to the supervisor after the interaction.
8. Translate narrated user feedback into a delta brief containing:
   - the new rule;
   - what it supersedes;
   - what remains unchanged;
   - whether creativity is open or constrained;
   - the evidence and acceptance check;
   - the instruction to avoid unrelated work.
9. Confirm Claude acknowledged a delivered delta before telling the user it was received or applied.
10. Inspect every permission or decision request surfaced by compact state. Approve only actions within the user's scope; redirect Claude when it proposes an unsafe, destructive, or needlessly broad operation.
11. Let Claude make normal engineering decisions within the chosen direction. Escalate only material user choices.
12. For small active-item refinements, ask Claude to edit, render, and screenshot in the same background run. Do not insert a fresh plan or broad rediscovery phase.

## Use proportionate verification

Match checks to the current stage and repository guidance:

| Stage | Default checks |
|---|---|
| Prototype loop | Render every variant, capture comparable screenshots, inspect browser or runtime errors, and understand the diff. Skip broad lint, typecheck, tests, and builds. |
| Small visual delta | Re-render the affected viewport and inspect the focused diff. Run a focused static check only when the repository makes it cheap or mandatory. |
| Chosen implementation checkpoint | Run focused lint, typecheck, and directly relevant tests for the touched package or component when available. |
| Auth, permissions, payments, data, migrations, security, or external effects | Run the relevant correctness checks before advancing; do not defer risk-critical validation for speed. |
| Final handoff, commit, push, or release | Follow repository guidance and run the risk-proportionate final suite. Run broad checks only when required by the repository or warranted by the change. |

Do not run the same broad suite after every visual refinement. Record deferred checks so they are not mistaken for completed validation.

## Maintain a Codex-owned work queue

Keep the ordered backlog in Codex, not in Claude's prompt or transcript. Do not preload future big-picture items into Claude.

Use the available plan or todo mechanism when possible:

- Keep exactly one big-picture item active or waiting on its user decision.
- Keep later items pending in user-selected order.
- Assign stable identifiers such as `Q1`, `Q2`, and `Q3`.
- Preserve each item's original user wording, intended outcome, creativity mode, dependencies, acceptance criteria, and later refinements.
- Mirror a compact user-visible queue snapshot after every add, reorder, merge, cancel, dispatch, or completion so the queue can be reconstructed after context compaction.
- Do not create a repository queue file unless the user explicitly requests cross-thread persistence.

Use these lanes:

| Lane | Classification | Action |
|---|---|---|
| Immediate interrupt | The user says stop, cancel, replace, or do this now; a safety issue appears; or continued work would waste effort because the active direction is invalid | Interrupt once at the nearest safe boundary, obtain a Claude prompt, and send a superseding active-item delta |
| Active-item delta | A small correction or clarification belongs to the current outcome and does not create a new big-picture task | Attach it to the active item and deliver it at the next prompt boundary; interrupt only when the user says now or delay would invalidate work |
| Queued item | A new feature, redesign, product direction, architectural slice, or other substantial outcome can wait until the active item completes | Record its queue position and do not send it to Claude |
| Decision gate | Claude needs an unresolved user choice for the active item | Keep the item active, ask the user, and do not dispatch the next big-picture item |

If classification is materially ambiguous, ask whether the user wants an immediate interruption or a queued item. Otherwise, default a new independent big-picture outcome to the queue.

When the user says `queue this`, acknowledge the identifier and position explicitly and state that it has not been sent to Claude.

When the user cancels or replaces the active item:

1. Stop Claude at the nearest safe boundary without killing the named conversation.
2. Ask Claude to report partial edits, commands still running, and any cleanup or verification needed.
3. Mark the old item superseded rather than completed.
4. Do not revert partial work automatically.
5. Dispatch the replacement only after the worktree is in an understood state.

Do not use Claude background agents as the master scheduler. Interactive or background execution may carry the active item, but Codex owns ordering, interruption, and dispatch.

## Dispatch the next queued item

Advance automatically when all dispatch gates hold:

1. Claude's exact background session reports `done`, or it has handed off a decision that the user resolved.
2. The stage-appropriate evidence and worktree review show a usable checkpoint.
3. Required user decisions for that item are resolved.
4. The next item's dependencies are satisfied.
5. The user has not paused, reordered, canceled, or replaced the queue.

Then:

1. Mark the active item complete and show the updated queue.
2. Re-read the next item's original wording and refinements.
3. Refresh only the repository and runtime facts that may have changed; do not repeat broad discovery or reuse a stale implementation brief.
4. Resolve any new contradiction or material user choice before dispatch.
5. Mark the next item active.
6. Compose a fresh brief in its correct task mode and send only that item to Claude.
7. Confirm Claude acknowledged the new active item.

Run release validation only at the final boundary or when repository policy or risk requires it. Use the stage-appropriate checks above at ordinary queue checkpoints.

If the queue is empty, preserve the Claude session ID and conversation. The supervisor may stop its idle process without losing resumable state.

## Own runtime access

When runtime access is required:

- Ensure the dev server runs from the exact checkout. Let Claude start and maintain it when its environment already has the required access; Codex handles access setup or recovery when it does not.
- Verify container mounts, ports, proxy mappings, and response provenance before giving Claude browser access.
- Do not assume a successful proxied URL serves local code; inspect the response or flow source.
- Give Claude the verified route and browser surface, then let it iterate without a Codex handoff between every edit and screenshot.
- Treat HTTP success, static checks, Claude's browser report, and Codex's browser review as separate evidence.
- Avoid irreversible UI actions or real-data mutation unless the user explicitly authorized them.
- Restore any reversible test mutation and verify restoration.

Follow repository-specific browser and simulator instructions over generic preferences in this skill.

## Review without becoming the designer

Inspect Claude's work independently.

- Send verified correctness, security, permissions, accessibility, data-integrity, and acceptance failures back to Claude with evidence.
- Do not convert a subjective Codex preference into a required fix.
- For subjective concerns, ask Claude for alternatives or present the concern and options to the user.
- Check that the implementation follows the user's selected concept rather than Codex's preferred interpretation.
- Check motion in context, including reduced motion and interruption behavior.
- Preserve unrelated user changes and inspect untracked files as well as diffs.

## Recover the conversation

Use this order:

1. Query the exact agent or session ID with the compact status helper.
2. If the state is `blocked` or `idle`, attach and answer only the active question.
3. If the state is `failed` or `stopped`, read recent logs once, understand partial edits, and use `claude respawn <agent-id>` only when continuing the same task is safe.
4. If the supervisor no longer lists the agent, resume the durable session ID from the exact repository root without overriding model or effort:

```bash
claude --resume <session-id>
```

5. Prefer the full session ID, then the exact short agent ID. Do not use `--continue` by default; it can attach to the wrong conversation when a directory has multiple sessions.
6. Use `--continue` only after proving there is exactly one relevant recent conversation and no ID is recoverable.
7. If Claude's MCP or browser configuration changed, resume the conversation so the new tool registry loads, then return it to the background.
8. If a process is stuck, resolve the exact process before terminating it. Do not use a broad kill pattern.
9. After resuming, ask Claude for a quiet continuity handoff: completed work, pending work, current restrictions, and next action. Compare it with Codex's state before proceeding.
10. Re-run the conditional preflight if the resumed session shows a session hook error or cannot use tools.

Do not promise that one OS process will remain alive forever. Promise continuity through the named, persisted Claude conversation and verified resume path.

Keep the master queue in Codex during recovery. Resume Claude with only the currently active item; do not reveal or dispatch later queue contents until their dispatch gates hold.

## Verify and hand off

Before calling the work complete:

1. Ask Claude to run the repository-native checks required by the change risk, repository guidance, and current stage.
2. Independently run the same critical checks and any final lint, typecheck, tests, build, or `git diff --check` commands that are actually required. Do not manufacture a broad suite when the repository and change do not warrant one.
3. Inspect Git status, staged files, unstaged files, and untracked files separately.
4. Complete browser or simulator verification from the required surface.
5. Record which results came from Claude and which Codex reproduced.
6. Preserve the Claude session until review is complete. Do not attach merely to keep its process alive.
7. Report implementation, selected design direction, validation, remaining gaps, worktree state, Claude session status, and any remaining queue items.

Do not commit, stage, push, deploy, delete, or expose secrets unless the user explicitly authorized that exact action.
