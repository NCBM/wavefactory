from wavefactory.mixing import fadeout
from wavefactory.synth import Harmox


_piano = Harmox([1, 0.9, 0.8, 0.7, 0.6, 0.4, 0.2])


class Piano:
    @staticmethod
    def synth(f: float, t: float, r: int):
        return fadeout(_piano.synth(f, t, r))