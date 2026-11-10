"""Small IO helpers shared by the CLI tools."""

from __future__ import annotations

import json
import sys

# TODO(mtanaka): expose a streaming writer for very large plans.


def load_config(path: str | None) -> dict:
    if path is None:
        # TODO(jkolb): read defaults from the packaged profile instead.
        return {"levels": {}}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_plan(plan: dict, stream) -> None:
    # TODO(hsato): pretty-print only when the stream is a tty.
    json.dump(plan, stream, indent=2, sort_keys=True)
    stream.write("\n")


def summarise_plan(plan: dict) -> str:
    # TODO(blundqvist): include the estimated memory footprint.
    return f"{len(plan)} cells scheduled"


# TODO: drop the unused json import guard in the next cleanup pass
