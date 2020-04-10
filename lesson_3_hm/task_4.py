def my_func(x, y):
    """ Возводит число (x) в степень (y)
    I способ
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Необходимо вводить числа')
    return x ** y if y < 0 else "Число (y) должно быть целым отрицательным"


def my_func_2(x, y):
    """ Возводит число (x) в степень (y)
    II способ
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Необходимо вводить числа')
    for i in range(abs(y)):
        x = 1 / x
    return x if y < 0 else "Число (y) должно быть целым отрицательным"


print(my_func(x=input('Введите положительное действительное число (x): '),
              y=input('Введите целое отрицательное число (y): ')))
print(my_func_2(x=input('Введите положительное действительное число (x): '),
                y=input('Введите целое отрицательное число (y): ')))
