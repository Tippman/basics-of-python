def division(val_1, val_2):
    """Возвращает результат деления двух чисел"""
    try:
        return int(val_1) / int(val_2)
    except ZeroDivisionError:
        return "Ошибка, на ноль делить нельзя!"


while True:
    ans = division(input("Введите числитель: "), input("Введите знаменатель: "))
    print(f"Результат деления - {round(ans, 2) if type(ans) == float else ans}")
    q = input("Повторить? y - да, n - нет ").upper()
    if q == "N":
        print("End!")
        break
    elif q == "Y":
        continue
    else:
        print("укажите только 'у' или 'n' на английской раскладке")
