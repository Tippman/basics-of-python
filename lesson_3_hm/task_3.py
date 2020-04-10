def my_func(*args):
    """Возвращает сумму двух максимальных элементов"""
    return sum(args) - min(args)


print(my_func(int(input('Введите первое число: ')),
              int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))
