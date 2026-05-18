import math

def roots(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        return "( )"
    if discriminante == 0:
        r1 = -b / (2 * a)
        return f"({r1})"
    r1 = (-b + math.sqrt(discriminante)) / (2 * a)
    r2 = (-b - math.sqrt(discriminante)) / (2 * a)
    return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * (x ** 2) + b * x + c

def to_string(a, b, c):
    if a == 0:
        if b == 0:
            return f"f(x) = {c}"
        return f"f(x) = {b} * X + {c}"
    if b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    if c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b,c):
    derivada_a = 2 * a
    if derivada_a == 0:
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {derivada_a} * X"
    return f"f'(x) = {derivada_a} * X + {b}"
