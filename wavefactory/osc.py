from math import sin, pi
from random import random

sine = sin
triangle = (
    lambda x: 4 / pi * abs((((x / 2 - pi / 4) % pi) + pi) % pi - pi / 2) - 1
)
square = (lambda x: (-1) ** int(x / pi))
sawtooth = (lambda x: (x / pi + 1) % 2 - 1)
noise = (lambda _: 2 * random() - 1)


def _root_iter(freq: float, phase: float, t: float, rate: int):
    return (
        2 * pi * freq * t for t in
        (i / rate for i in range(int(phase * rate), int((t + phase) * rate)))
    )


def no_wave(_, __, t: float, r: int):
    return [0.] * int(t * r)


def sine_wave(f: float, p: float, t: float, r: int):
    return map(sine, _root_iter(f, p, t, r))


def triangle_wave(f: float, p: float, t: float, r: int):
    return map(triangle, _root_iter(f, p, t, r))


def square_wave(f: float, p: float, t: float, r: int):
    return map(square, _root_iter(f, p, t, r))


def sawtooth_wave(f: float, p: float, t: float, r: int):
    return map(sawtooth, _root_iter(f, p, t, r))


def noise_wave(_, __, t: float, r: int):
    return map(noise, _root_iter(0, 0, t, r))