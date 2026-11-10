"""Tokeniser and expression parser for Orbit input decks."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

# TODO(mokonkwo): support nested section overrides in the loader.
MAX_DEPTH = 12


@dataclass
class Token:
    kind: str
    value: str
    line: int


def tokenize(text: str) -> Iterator[Token]:
    for lineno, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.split("#", 1)[0].strip()
        if not stripped:
            continue
        for chunk in stripped.split():
            yield Token("word", chunk, lineno)


def parse_sections(tokens: list[Token]) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current = "default"
    for token in tokens:
        if token.kind == "word" and token.value.endswith(":"):
            # TODO(trenner): validate that section names are unique.
            current = token.value[:-1]
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(token.value)
    return sections


def load(text: str) -> dict[str, list[str]]:
    # TODO(sbrann): emit a structured error with the offending line number.
    return parse_sections(list(tokenize(text)))


def dump(sections: dict[str, list[str]]) -> str:
    lines = []
    for name, values in sections.items():
        lines.append(f"{name}: {' '.join(values)}")
    # TODO(mokonkwo): drop the trailing newline for round-trip parity.
    return "\n".join(lines) + "\n"

# TODO(dmarino): cache token streams for repeated include resolution.
