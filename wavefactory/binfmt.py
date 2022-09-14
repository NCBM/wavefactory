from struct import pack, unpack
from typing import Iterable, Literal, Union

Bytes = Union[bytes, bytearray]


def duplicate(sample: Iterable[float], n: int = 2):
    if n < 1:
        raise ValueError("duplicate times must be greater than 0")
    for d in sample:
        for _ in range(n):
            yield d


def _signed_enc(
    sample: Iterable[int], depth: int, byteorder: Literal["little", "big"]
):
    res = bytearray()
    for p in (q.to_bytes(depth, byteorder, signed=True) for q in sample):
        res.extend(p)
    return res


def _float_enc(sample: Iterable[float], byteorder: Literal["little", "big"]):
    res = bytearray()
    if byteorder == "little":
        bos = "<"
    elif byteorder == "big":
        bos = ">"
    else:
        raise ValueError("byte order must be little or big")
    for q in sample:
        res.extend(pack(f"{bos}f", q))


def _signed_dec(
    data: Bytes, depth: int, byteorder: Literal["little", "big"]
):
    pos = 0
    while pos < len(data):
        yield int.from_bytes(data[pos:pos + depth], byteorder, signed=True)
        pos += depth


def _float_dec(data: Bytes, byteorder: Literal["little", "big"]):
    if byteorder == "little":
        bos = "<"
    elif byteorder == "big":
        bos = ">"
    else:
        raise ValueError("byte order must be little or big")
    pos = 0
    while pos < len(data):
        yield unpack(f"{bos}f", data[pos:pos + 4])
        pos += 4


class Encoder:
    @staticmethod
    def s16le(s: Iterable[int]):
        return _signed_enc(s, 2, "little")

    @staticmethod
    def s16be(s: Iterable[int]):
        return _signed_enc(s, 2, "big")

    @staticmethod
    def s24le(s: Iterable[int]):
        return _signed_enc(s, 3, "little")

    @staticmethod
    def s24be(s: Iterable[int]):
        return _signed_enc(s, 3, "big")

    @staticmethod
    def f32le(s: Iterable[float]):
        return _float_enc(s, "little")

    @staticmethod
    def f32be(s: Iterable[float]):
        return _float_enc(s, "big")


class Decoder:
    @staticmethod
    def s16le(b: Bytes):
        return _signed_dec(b, 2, "little")

    @staticmethod
    def s16be(b: Bytes):
        return _signed_dec(b, 2, "big")

    @staticmethod
    def s24le(b: Bytes):
        return _signed_dec(b, 3, "little")

    @staticmethod
    def s24be(b: Bytes):
        return _signed_dec(b, 3, "big")

    @staticmethod
    def f32le(b: Bytes):
        return _float_dec(b, "little")

    @staticmethod
    def f32be(b: Bytes):
        return _float_dec(b, "big")