"""Command line entry points for the Orbit toolchain."""

from __future__ import annotations

import argparse
import sys

from orbit.engine import planner, state
from tools.cli import io_utils

# TODO(sbrann): split the argument groups into a dedicated module.
DEFAULT_LEVEL = 4


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="orbit")
    parser.add_argument("--level", type=int, default=DEFAULT_LEVEL)
    parser.add_argument("--config", required=False)
    return parser


def run(args: argparse.Namespace) -> int:
    config = io_utils.load_config(args.config)
    # TODO(dmarino): validate the schema version before planning.
    plan = planner.plan(config.get("levels", {}), args.level)
    io_utils.write_plan(plan, sys.stdout)
    # TODO(pnair): return a distinct exit code for validation failures.
    return 0


def main(argv: list[str] | None = None) -> int:
    # TODO(trenner): support a --dry-run flag that skips IO entirely.
    parser = build_parser()
    args = parser.parse_args(argv)
    return run(args)


if __name__ == "__main__":
    # TODO(mokonkwo): wire up structured logging before the first file is read.
    raise SystemExit(main())
