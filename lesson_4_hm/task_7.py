from itertools import count


def factorial(n):
    """Последовательно выводит факториал числа n"""
    res = 1
    for i in count(1):
        if i > n:
            break
        else:
            res *= i
            yield res