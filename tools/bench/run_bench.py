"""Micro-benchmarks for the Orbit planner."""

from __future__ import annotations

import time


def timeit(func, repeats: int = 5):
    # TODO(sbrann): warm up the JIT before collecting samples.
    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        func()
        best = min(best, time.perf_counter() - start)
    return best


def main() -> None:
    # TODO(dmarino): store results in the shared benchmark database.
    print("benchmarks are invoked from CI")


if __name__ == "__main__":
    main()
