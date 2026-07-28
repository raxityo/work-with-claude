#!/usr/bin/env python3
"""Return one compact Claude background-agent status record."""

from __future__ import annotations

import json
import subprocess
import sys


ATTENTION_STATES = {"blocked", "idle", "failed", "stopped"}
TERMINAL_STATES = {"done", "failed", "stopped"}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: claude_agent_status.py <agent-id-or-session-id>", file=sys.stderr)
        return 2

    target = sys.argv[1]
    try:
        result = subprocess.run(
            ["claude", "agents", "--json", "--all"],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except subprocess.TimeoutExpired:
        print("claude agents timed out", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"could not run claude agents: {error}", file=sys.stderr)
        return 2
    if result.returncode:
        print(result.stderr.strip() or "claude agents failed", file=sys.stderr)
        return result.returncode

    try:
        agents = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        print(f"invalid claude agents output: {error}", file=sys.stderr)
        return 2
    if not isinstance(agents, list):
        print("invalid claude agents output: expected a list", file=sys.stderr)
        return 2

    exact = [
        agent
        for agent in agents
        if target in {agent.get("id"), agent.get("sessionId")}
    ]
    matches = exact or [
        agent
        for agent in agents
        if str(agent.get("id", "")).startswith(target)
        or str(agent.get("sessionId", "")).startswith(target)
    ]
    if len(matches) != 1:
        reason = "not found" if not matches else "ambiguous"
        print(json.dumps({"found": False, "reason": reason}, separators=(",", ":")))
        return 1

    agent = matches[0]
    state = agent.get("state", "unknown")
    print(
        json.dumps(
            {
                "found": True,
                "id": agent.get("id"),
                "sessionId": agent.get("sessionId"),
                "state": state,
                "attention": state in ATTENTION_STATES,
                "terminal": state in TERMINAL_STATES,
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
