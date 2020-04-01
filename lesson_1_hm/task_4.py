user_number = int(input('Введите целое положительное число - '))
max_number = 1
while True:
    if user_number % 10 > max_number:
        max_number = user_number % 10
        user_number = user_number // 10
    else:
        user_number = user_number // 10
    if user_number // 10 == 0:
        if user_number % 10 > max_number:
            max_number = user_number % 10
            break
        else:
            break
print(max_number)
