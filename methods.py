from prettytable import PrettyTable

from func import *
from decimal import Decimal


def half_division(a, b, delta):
    print('Метод половинного деления')
    table = PrettyTable()
    table.field_names = ["№ шага", "a", "b"]
    for i in range(1, 26):
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        f1 = f(x1)
        f2 = f(x2)
        table.add_row([i, a, b])
        if f1 > f2:
            a = x1
        else:
            b = x2
        if abs(b - a) <= 2 * delta:
            print('Достигнут критерий окончания '
                  'итерационного процесса.')
            break
    xm = (a + b) / 2
    ym = f(xm)
    print(table)
    print('xm = ' + str(xm) +
          '\t\tym = ' + str(ym))
    print()


def golden_ratio(a, b, eps):
    print('Метод золотого сечения')
    table = PrettyTable()
    table.field_names = ["№ шага", "a", "b"]

    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618 * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    for i in range(1, 26):
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = a + 0.618 * (b - a)
            f1 = f2
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + 0.382 * (b - a)
            f2 = f1
            f1 = f(x1)
        table.add_row([i, a, b])
        if abs(b - a) < eps:
            print('Достигнут критерий окончания '
                  'итерационного процесса.')
            break
    xm = (a + b) / 2
    ym = f(xm)

    print(table)
    print('xm = ' + str(xm) +
          '\t\tym = ' + str(ym))
    print()


def newton(a, b, eps):
    print('Метод Ньютона')
    table = PrettyTable()
    table.field_names = ["№ шага", f"x{chr(0x2096)}",
                         f"f'(x{chr(0x2096)})"]
    x = (a + b) / 2
    x1 = 0
    for i in range(1, 26):
        if abs(first_derivative(x)) <= eps:
            print('Достигнут критерий окончания '
                  'итерационного процесса.')
            break
        x1 = x - first_derivative(x) / second_derivative(x)
        table.add_row([i, x1, "e^".join("{:.2e}".format(first_derivative(x1)).split("e"))])
        x = x1
    print(table)
    print('xm = ' + str(x1) + '\t\tym = ' + str(f(x1)))
    print()
