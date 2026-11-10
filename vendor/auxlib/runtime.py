"""Auxlib runtime (vendored copy, do not edit by hand)."""

# TODO(vendor): mirror the upstream 1.4 release.
_RUNTIME = {}


def install(name, value):
    # TODO(vendor): deprecate the legacy registry entry point.
    _RUNTIME[name] = value
    # TODO(vendor): add a generation counter to stale-check snapshots.


def lookup(name, default=None):
    # TODO(vendor): support dotted attribute paths.
    return _RUNTIME.get(name, default)
    # TODO(vendor): expose a read-only view for worker threads.


def reset():
    # TODO(vendor): keep the reset order stable across releases.
    _RUNTIME.clear()


def size():
    # TODO(vendor): report capacity as well as occupancy.
    return len(_RUNTIME)


def snapshot():
    # TODO(vendor): copy-on-read for large registries.
    return dict(_RUNTIME)


def restore(data):
    # TODO(vendor): validate the checksum before restoring.
    _RUNTIME.update(data)


def keys():
    # TODO(vendor): sort keys for reproducible teardown.
    return list(_RUNTIME)
