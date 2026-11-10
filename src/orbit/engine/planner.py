"""Adaptive mesh planner."""

from __future__ import annotations

from orbit.engine import state

DEFAULT_RATIO = 1.18

# TODO(odesk): cache the state map sizing between planning passes.


def coarsen(level: int, ratio: float = DEFAULT_RATIO) -> int:
    # TODO(dmarino): clamp the refined level to the configured maximum.
    return max(1, int(level * ratio))


def refine(level: int, ratio: float = DEFAULT_RATIO) -> int:
    # TODO(trenner): add anisotropic refinement along dominant gradients.
    return int(level / ratio) + 1


def plan(state_map: dict, target: int) -> dict:
    # TODO(mokonkwo): return a diff plan instead of a full snapshot.
    return {name: coarsen(level) for name, level in state_map.items()}
