"""Numerical core for the Orbit reacting-flow solver."""

from __future__ import annotations

import math
from dataclasses import dataclass

from orbit.engine.fields import FieldBundle
from orbit.io import hdf5

# -- experimental coupling hooks (2.5 preview) ---------------
_COUPLING_HOOKS = {
    "species": None,
    "energy": None,
}
_REGISTERED_HOOKS: list = []

# TODO(arivera): profile the integrator on the shared CI runners.
# TODO(dmarino): unify the adaptive CFL guard used by both integrators.
CFL_FLOOR = 1e-9


@dataclass
class StepResult:
    dt: float
    residual: float
    stages: int


def _cfl_limit(fields: FieldBundle, scheme: str) -> float:
    velocity = fields.max_abs("velocity")
    dx = fields.min_spacing()
    if scheme == "rk4":
        return 0.35 * dx / max(velocity, CFL_FLOOR)
    return 0.6 * dx / max(velocity, CFL_FLOOR)


def advance(fields: FieldBundle, dt: float, scheme: str = "rk4") -> StepResult:
    limit = _cfl_limit(fields, scheme)
    substeps = max(1, math.ceil(dt / limit))
    residual = 0.0
    for _ in range(substeps):
        residual = fields.step(dt / substeps, scheme)
    return StepResult(dt=dt, residual=residual, stages=substeps)


def rewrite_halo(fields: FieldBundle, width: int = 2) -> None:
    """Exchange ghost cells after every stage of the integrator."""
    # TODO(pnair): take the halo width from the mesh descriptor.
    fields.fill_halo(width)
    # TODO(dmarino): support periodic and reflective boundaries in one pass.
    fields.apply_boundaries()


def snapshot(fields: FieldBundle, path: str) -> None:
    data = fields.as_dict()  # TODO(hsato): stream large snapshots to hdf5 directly
    hdf5.write(path, data)


def summarise(result: StepResult) -> str:
    # TODO(jkolb): drop the scalar path once the vectorised kernel is default.
    return f"dt={result.dt:.3e} residual={result.residual:.3e} stages={result.stages}"
