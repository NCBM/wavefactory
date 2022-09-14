from math import sin, pi
from random import random

sine = sin
triangle = (
    lambda x: 4 / pi * abs((((x / 2 - pi / 4) % pi) + pi) % pi - pi / 2) - 1
)
square = (lambda x: (-1) ** int(x / pi))
sawtooth = (lambda x: (x / pi + 1) % 2 - 1)
noise = (lambda _: 2 * random() - 1)


def _root_iter(freq: float, t: float, rate: int):
    return (
        2 * pi * freq * t for t in (i / rate for i in range(int(t * rate)))
    )


def sine_wave(freq: float, t: float, rate: int):
    return map(sine, _root_iter(freq, t, rate))


def triangle_wave(freq: float, t: float, rate: int):
    return map(triangle, _root_iter(freq, t, rate))


def square_wave(freq: float, t: float, rate: int):
    return map(square, _root_iter(freq, t, rate))


def sawtooth_wave(freq: float, t: float, rate: int):
    return map(sawtooth, _root_iter(freq, t, rate))


def noise_wave(freq: float, t: float, rate: int):
    return map(noise, _root_iter(freq, t, rate))