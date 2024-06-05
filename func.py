from math import sin, cos


def f(x):
    return x ** 2 + x + sin(x)


def first_derivative(x):
    return 2 * x + 1 + cos(x)


def second_derivative(x):
    return 2 - sin(x)
