from methods import *


def get_input():
    try:
        return input('> ').strip()
    except (EOFError, KeyboardInterrupt):
        print('Завершение работы программы...')
        exit()


def start():
    print('Численные методы нахождения экстремума функции.')
    print('Исходная функция: f(x) = x^2 + x + sin(x)\n')
    while True:
        print('Выберите метод решения задачи.')
        print('1 - метод половинного деления; 2 - метод золотого сечения; 3 - метод Ньютона')
        ans = get_input()
        a = -1
        b = 0
        eps = 0.0000000001
        match ans:
            case '1':
                half_division(a, b, eps)
            case '2':
                golden_ratio(a, b, eps)
            case '3':
                newton(a, b, eps)
            case _:
                print('Выберите один из доступных методов.')
