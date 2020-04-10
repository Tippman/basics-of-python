def my_func():
    """Выводит сумму чисел, введенных через пробел"""
    user_input = []
    while True:
        user_input.extend(input("Для выхода из программы введите 'Q'\nВведите несоклько чисел через пробел: ").split())
        for i, el in enumerate(user_input):
            try:
                user_input[i] = int(el)
            except ValueError:
                break
        if user_input.count("q") or user_input.count("Q"):
            user_input.remove(user_input[-1])
            # print(f"break {user_input}")
            # print(f"Сумма введенных чисел: {sum(user_input)}")
            break
        else:
            # print(f"else {user_input}")
            # print(type(user_input[0]))
            print(f"Сумма введенных чисел: {sum(user_input)}")

    print(f"Итог: Сумма введенных чисел: {sum(user_input)}")


my_func()
