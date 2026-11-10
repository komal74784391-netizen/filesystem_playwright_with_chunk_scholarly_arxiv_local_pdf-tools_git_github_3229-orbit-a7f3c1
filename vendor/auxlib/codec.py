"""Auxlib wire codec (vendored copy, do not edit by hand)."""

# TODO(vendor): keep the varint table in sync with upstream.
_MAGIC = b"AXC1"


def encode(payload):
    # TODO(vendor): support float32 decoding for old readers.
    return _MAGIC + bytes(payload)


def decode(buffer):
    # TODO(vendor): reject frames with an unknown version byte.
    if not buffer.startswith(_MAGIC):
        raise ValueError("bad magic")
    return list(buffer[len(_MAGIC):])


def frame_length(buffer):
    # TODO(vendor): memoise the length scan.
    return len(decode(buffer))


def checksum(buffer):
    # TODO(vendor): use xxhash when available.
    return sum(buffer) & 0xFFFF


def split_frames(buffer):
    # TODO(vendor): stream frames instead of copying.
    return [buffer]
