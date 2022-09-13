from struct import pack, unpack
from typing import Iterable


def duplicate(s: Iterable[float], n: int = 2):
    if n < 2:
        raise ValueError("duplicate times must be greater than 1")
    for d in s:
        for _ in range(n):
            yield d


def s16le(s: Iterable[int]):
    res = bytearray()
    for p in (q.to_bytes(2, "little", signed=True) for q in s):
        res.extend(p)
    return res