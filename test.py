from wavefactory.generator import (
    sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave
)
from wavefactory.binfmt import duplicate, Encoder
import wave

from wavefactory.mixing import Mixer, PackedWave


for f in (sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave):
    c = f(260, 0, 1, 44100)
    c2 = f(520, 0, 1, 44100)
    c3 = f(260 * 3, 0, 1, 44100)
    m = Mixer()
    m += PackedWave(c, 44100)
    m += PackedWave(c2, 44100)
    m += PackedWave(c3, 44100)
    with wave.open(f"{f.__name__}.wav", "w") as fi:
        fi.setnchannels(2)
        fi.setsampwidth(2)
        fi.setframerate(44100)
        fi.writeframes(Encoder.s16le(int(v * 32767) for v in duplicate(m.mix(44100))))