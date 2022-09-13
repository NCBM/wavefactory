from math import sin, pi

sine = sin
triangle = (
    lambda x: 4 / pi * abs((((x / 2 - pi / 4) % pi) + pi) % pi - pi / 2) - 1
)
square = (lambda x: (-1) ** int(x / pi))
sawtooth = (lambda x: (x / pi + 1) % 2 - 1)


def _root_iter(f: float, t: float, r: int):
    return (2 * pi * f * t for t in (i / r for i in range(int(t * r))))


def sine_wave(f: float, t: float, r: int):
    return map(sine, _root_iter(f, t, r))


def triangle_wave(f: float, t: float, r: int):
    return map(triangle, _root_iter(f, t, r))


def square_wave(f: float, t: float, r: int):
    return map(square, _root_iter(f, t, r))


def sawtooth_wave(f: float, t: float, r: int):
    return map(sawtooth, _root_iter(f, t, r))