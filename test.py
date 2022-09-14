from wavy.generator import (
    sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave
)
from wavy.binfmt import duplicate, Encoder
import wave


for f in (sine_wave, triangle_wave, square_wave, sawtooth_wave, noise_wave):
    d = f(261, 1, 44100)
    with wave.open(f"{f.__name__}.wav", "w") as fi:
        fi.setnchannels(2)
        fi.setsampwidth(2)
        fi.setframerate(44100)
        fi.writeframes(Encoder.s16le(int(v * 32767) for v in duplicate(d)))