from wavefactory.binfmt import duplicate, Encoder
import wave
from wavefactory.mixing import fadeout

from wavefactory.synth import Harmox


with wave.open("test.wav", "w") as fi:
    h = Harmox()
    harm = [1, 0.9, 0.8, 0.7, 0.6, 0.4, 0.2]
    # for i in range(5, 2, -1):
    #     harm.append(i / 5)
    h.harm = harm
    fi.setnchannels(2)
    fi.setsampwidth(2)
    fi.setframerate(44100)

    def ww(f, t):
        w = fadeout(h.synth(f, t, 44100))
        fi.writeframes(Encoder.s16le(int(v * 0x7FFF) for v in duplicate(w)))

    for freq, dura in [
        (261.6, 0.5),  # C4
        (261.6, 0.5),  # C4
        (392.0, 0.5),  # G4
        (392.0, 0.5),  # G4
        (440.0, 0.5),  # A4
        (440.0, 0.5),  # A4
        (392.0, 1.0),  # G4

        (349.2, 0.5),  # F4
        (349.2, 0.5),  # F4
        (329.6, 0.5),  # E4
        (329.6, 0.5),  # E4
        (293.6, 0.5),  # D4
        (293.6, 0.5),  # D4
        (261.6, 1.0),  # C4

        (392.0, 0.5),  # G4
        (392.0, 0.5),  # G4
        (349.2, 0.5),  # F4
        (349.2, 0.5),  # F4
        (329.6, 0.5),  # E4
        (329.6, 0.5),  # E4
        (293.6, 1.0),  # D4

        (392.0, 0.5),  # G4
        (392.0, 0.5),  # G4
        (349.2, 0.5),  # F4
        (349.2, 0.5),  # F4
        (329.6, 0.5),  # E4
        (329.6, 0.5),  # E4
        (293.6, 1.0),  # D4

        (261.6, 0.5),  # C4
        (261.6, 0.5),  # C4
        (392.0, 0.5),  # G4
        (392.0, 0.5),  # G4
        (440.0, 0.5),  # A4
        (440.0, 0.5),  # A4
        (392.0, 1.0),  # G4

        (349.2, 0.5),  # F4
        (349.2, 0.5),  # F4
        (329.6, 0.5),  # E4
        (329.6, 0.5),  # E4
        (293.6, 0.5),  # D4
        (293.6, 0.5),  # D4
        (261.6, 1.0),  # C4
    ]:
        ww(freq, dura)