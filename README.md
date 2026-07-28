# Work with Claude

A Codex skill for orchestrating a persistent Claude Code CLI conversation while Codex remains the main coordinator.

Claude acts as an independent designer and implementation engineer. Codex owns the environment, permissions, user communication, work queue, technical review, and independent verification.

Fast iteration is the default: Claude runs as a supervised background agent, performs a conditional environment check, and continues directly into reversible local edits. Codex checks compact status instead of streaming Claude's transcript. For open-ended UI work, Claude creates, renders, and screenshots at least three distinct prototypes before asking you to choose.

## Install in Codex

Run one command:

```bash
npx skills add raxityo/work-with-claude --skill work-with-claude -g -a codex -y
```

Then restart Codex and start a new task so the installed skill is discovered.

### Install through Codex

You can also ask Codex:

```text
Use $skill-installer to install this skill:
https://github.com/raxityo/work-with-claude/tree/main/skills/work-with-claude
```

## Requirements

- Codex
- A recent Claude Code CLI installed and authenticated; older versions without background-agent support use the interactive fallback
- Node.js with `npx` for the one-command installer

Confirm Claude Code is available:

```bash
claude --version
claude auth status
```

This skill does not install Claude Code or bypass its permission system.

## Use

Ask Codex explicitly to use the skill:

```text
Use $work-with-claude to have Claude redesign this interface as an independent
designer and front-end engineer. Build three distinct prototypes and show me
comparable screenshots before I choose.
```

You can narrate refinements while Claude works:

```text
Queue the upload-flow redesign for later. For the active navigation work, change the
selection treatment to a neutral color right now.
```

Codex will keep substantial later work in its own ordered queue and send only the active big-picture item to Claude.

### Control Claude's reporting

Quiet reporting is the default. It limits only Claude's progress narration and final handoff length, not its design exploration, implementation depth, tool use, or number of prototypes.

```text
Use $work-with-claude for this redesign. Keep Claude reporting quiet.
```

Ask for more explanation when useful:

```text
Use standard Claude reporting for this task.
Use detailed Claude reporting for the final architecture review.
```

Claude Code does not currently expose a reliable `--quiet` token-control flag. The skill enforces reporting detail in the task brief and keeps Codex from reading the live background transcript.

## What the skill handles

- Persistent named Claude Code conversations
- Native background-agent execution with compact status-only monitoring
- Quiet handoffs by default without limiting Claude's creativity or engineering depth
- Optional standard or detailed Claude reporting when requested
- Immediate reversible edits with minimal startup ceremony
- Three materially different rendered prototypes with comparable screenshots
- User selection after prototypes exist, without Codex choosing a direction
- Directed implementation and constrained-creativity modes
- Design and animation skill guidance
- Automatic Claude permissions when supported and safe, with `acceptEdits` fallback
- Risk- and repository-dependent verification instead of full checks after every iteration
- Permission and publication boundaries
- Immediate corrections versus queued big-picture work
- Claude session recovery
- Runtime, browser, test, and worktree verification

## Update

```bash
npx skills update work-with-claude -g -y
```

## Remove

```bash
npx skills remove work-with-claude -g -a codex -y
```

## Repository layout

```text
skills/
└── work-with-claude/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── scripts/
    │   └── claude_agent_status.py
    └── references/
        ├── fast-start-prompts.md
        └── prompt-patterns.md
```

The `skills/work-with-claude` layout is discoverable by the `skills` CLI and compatible with skills.sh.
