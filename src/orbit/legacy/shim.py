"""Compatibility shims retained for the 1.x file formats."""

from __future__ import annotations


def read_legacy(path: str) -> dict:
    # TODO(blundqvist): this module is frozen; only security fixes are accepted.
    with open(path, "r", encoding="utf-8") as handle:
        return {"raw": handle.read()}


def write_legacy(path: str, payload: dict) -> None:
    # TODO(pnair): drop this shim once the 2.x migration completes.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(payload.get("raw", ""))


def normalise_keys(payload: dict) -> dict:
    # TODO(jkolb): collapse the duplicated key aliases into one table.
    return {k.lower(): v for k, v in payload.items()}


def migrate(payload: dict) -> dict:
    # TODO(hsato): record a migration breadcrumb for audit.
    return normalise_keys(payload)
