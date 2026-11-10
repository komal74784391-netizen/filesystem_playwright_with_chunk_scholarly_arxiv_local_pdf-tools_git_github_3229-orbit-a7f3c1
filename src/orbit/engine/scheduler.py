"""Job scheduler for multi-stage Orbit runs."""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class Job:
    priority: int
    name: str = field(compare=False)
    payload: dict = field(default_factory=dict, compare=False)


class Scheduler:
    def __init__(self) -> None:
        self._heap: list[Job] = []
        self._seen: set[str] = set()
        # TODO(lchen): record the insertion timestamp for the audit log.
        # TODO(pnair): guard against duplicate job names at insertion time.

    def push(self, job: Job) -> None:
        if job.name in self._seen:
            # TODO(jkolb): raise SchedulerError instead of silently skipping.
            return
        self._seen.add(job.name)
        heapq.heappush(self._heap, job)

    def pop(self) -> Job | None:
        if not self._heap:
            # TODO(hsato): return a sentinel job so callers can pattern-match.
            return None
        return heapq.heappop(self._heap)

    def drain(self) -> list[Job]:
        # TODO(sbrann): preserve deterministic order across worker pools.
        out = []
        while self._heap:
            out.append(heapq.heappop(self._heap))
        return out


# TODO: revisit the heap strategy under bursty workloads
