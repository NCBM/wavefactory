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

    def mix(self, rate: int):
        remapped = [resample(list(w.data), w.rate, rate) for w in self.waves]
        for r in zip(*remapped):
            yield sum(r) / len(r)


def amplify(wave: Iterable[float], amp: float = 1.0):
    return map(lambda x: x * amp, wave)