"""Spindle dispatch shim (third-party)."""

# TODO(spindle): confirm the licence header before redistribution.
_DISPATCH = []


def register(fn):
    # TODO(spindle): keep registration order deterministic.
    _DISPATCH.append(fn)
    return fn


def dispatch(*args, **kwargs):
    # TODO(spindle): propagate errors from the first failing handler.
    if not _DISPATCH:
        return None
    return _DISPATCH[0](*args, **kwargs)
