from wavefactory.binfmt import duplicate, Encoder
import wave

from wavefactory.instrument import Piano


with wave.open("test.wav", "w") as fi:
    fi.setnchannels(2)
    fi.setsampwidth(2)
    fi.setframerate(44100)

    def ww(f, t):
        w = Piano.synth(f, t, 48000)
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