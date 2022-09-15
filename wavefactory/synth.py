from typing import Dict, List, Optional, Union

from wavefactory.mixing import Mixer, PackedWave, amplify
from wavefactory.osc import sine_wave


class Harmox:
    def __init__(self, harm: Optional[List[float]] = None) -> None:
        self._harm: List[float] = [] if harm is None else harm
        self.vol: float = 1.

    @property
    def harm(self):
        return self._harm

    @harm.setter
    def harm(self, h: Union[List[float], Dict[int, float]]):
        if isinstance(h, list):
            self._harm = h
        elif isinstance(h, dict):
            self._harm = [0.] * max(h.keys())
            for k, v in h.items():
                self._harm[k] = v
        else:
            raise TypeError("expecting a list or a dict")

    def synth(self, freq: float, t: float, rate: int):
        m = Mixer()
        sw = (lambda f: sine_wave(f, 0, t, rate))
        for i, v in enumerate(self.harm, 1):
            m += PackedWave(amplify(sw(i * freq), v), rate)
        return m.mix(rate)