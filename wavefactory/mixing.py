from dataclasses import dataclass
from typing import Iterable, List

from wavefactory.resampling import resample


@dataclass
class PackedWave:
    data: Iterable[float]
    rate: int


class Mixer:
    def __init__(self) -> None:
        self.waves: List[PackedWave] = []

    def __add__(self, other: PackedWave):
        self.waves.append(other)
        return self

    def extend(self, it):
        self.waves.extend(it)

    def mix(self, rate: int):
        remapped = [resample(list(w.data), w.rate, rate) for w in self.waves]
        for r in zip(*remapped):
            yield sum(r) / len(r)


def amplify(wave: Iterable[float], amp: float = 1.):
    return map(lambda x: x * amp, wave)


def fadein(wave: Iterable[float]):
    li = list(wave)
    for i, w in enumerate(li, 1):
        yield w * i / len(li)


def fadeout(wave: Iterable[float]):
    li = list(wave)
    for i, w in enumerate(li, 1):
        yield w * (1 - i / len(li))


def volfade(wave: Iterable[float], start: float = 0., end: float = 1.):
    li = list(wave)
    for i, w in enumerate(li, 1):
        yield w * (start + i * (end - start) / len(li))