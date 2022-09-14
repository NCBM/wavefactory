from typing import List


def resample(wave: List[float], srcrate: int, dstrate: int):
    for n in range(len(wave) * dstrate // srcrate):
        loc = n * srcrate / dstrate
        if int(loc) + 1 >= len(wave):
            yield wave[int(loc)]
            return
        d = wave[int(loc) + 1] - wave[int(loc)]
        yield wave[int(loc)] + d * (loc % 1)