from typing import Dict, List, Union

from wavefactory.mixing import Mixer, PackedWave, amplify
from wavefactory.osc import sine_wave


class Harmox:
    def __init__(self) -> None:
        self.harm: List[float] = []
        self.vol: float = 1.

    def set_harm(self, h: Union[List[float], Dict[int, float]]):
        if isinstance(h, list):
            self.harm = h
        elif isinstance(h, dict):
            self.harm = [0.] * max(h.keys())
            for k, v in h.items():
                self.harm[k] = v
        else:
            raise TypeError("expecting a list or a dict")

    def synth(self, freq: float, t: float, rate: int):
        m = Mixer()
        sw = (lambda f: sine_wave(f, 0, t, rate))
        m.waves.extend(
            PackedWave(amplify(sw(i * freq), v), rate)
            for i, v in enumerate(self.harm, 1)
        )