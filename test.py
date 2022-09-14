from wavefactory.osc import (
    sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave
)
from wavefactory.binfmt import duplicate, Encoder
import wave

from wavefactory.mixing import Mixer, PackedWave


for f in (sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave):
    tf = lambda x: f(x, 0, 1, 44100)
    c, c2, c3, c4 = tf(260), tf(260 * 2), tf(260 * 3), tf(260 * 4)
    m = Mixer()
    m += PackedWave(c, 44100)
    m += PackedWave(c2, 44100)
    m += PackedWave(c3, 44100)
    m += PackedWave(c4, 44100)
    with wave.open(f"{f.__name__}.wav", "w") as fi:
        fi.setnchannels(2)
        fi.setsampwidth(2)
        fi.setframerate(48000)
        fi.writeframes(Encoder.s16le(int(v * 0x5FFF) for v in duplicate(m.mix(48000))))