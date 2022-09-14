from wavefactory.binfmt import duplicate, Encoder
import wave
from wavefactory.mixing import fadeout

from wavefactory.synth import Harmox


with wave.open("test.wav", "w") as fi:
    h = Harmox()
    harm = [1, 0.9, 0.8, 0.7, 0.6]
    # for i in range(5, 2, -1):
    #     harm.append(i / 5)
    h.harm = harm
    w = h.synth(440, 1, 44100)
    w = fadeout(w)
    fi.setnchannels(2)
    fi.setsampwidth(2)
    fi.setframerate(44100)
    fi.writeframes(Encoder.s16le(int(v * 0x7FFF) for v in duplicate(w)))