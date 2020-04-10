def int_func(user_input):
    """Возвращает все введенные слова с большой буквы"""
    user_input = user_input.split()
    for i, el in enumerate(user_input):
        user_input[i] = el[0].upper() + el[1:]
    print(" ".join(user_input))


int_func(input("Введите несколько слов через пробел: "))
