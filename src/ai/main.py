#!/usr/bin/env python3
"""
main.py
Entry point for Everything-AI.
Presumed need: runnable CLI after creating the runtime + builders.
"""

from __future__ import annotations
import sys
from pathlib import Path

# Make package importable when run as python -m src.ai.main
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ai.core.runtime import EverythingAI


def main() -> None:
    goal = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "build a hello world module"
    print(f"Everything-AI starting for goal → {goal!r}")
    ai = EverythingAI()
    outcome = ai.run(goal)
    print("\n=== Delivery Summary ===")
    print(f"Steps planned : {outcome['steps']}")
    for art in outcome["results"].get("artifacts", []):
        print(f"  ✓ {art['step']}: {art['output']}")
    if outcome["results"].get("errors"):
        print("Errors:")
        for e in outcome["results"]["errors"]:
            print(f"  ✗ {e['step']}: {e['error']}")
    print(f"\nArtifacts live under: {outcome['generated_dir']}")
    print("Everything-AI cycle complete.")


if __name__ == "__main__":
    main()
