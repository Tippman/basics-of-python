from itertools import count, cycle


def rnd_nmb_from(start_number):
    """Выводит последовательно числа, начиная с указанного"""
    some_numbers = []
    for i in count(start_number):
        if i > 20:
            break
        else:
            some_numbers.append(i)
    return some_numbers


def cycle_from_list(some_list, count_f):
    """Выводит каждый элемент строки в список нужное количество раз"""
    break_point = 0
    res = []
    for f in cycle(some_list):
        if break_point > count_f:
            break
        else:
            break_point += 1
        res.append(f)
    return res