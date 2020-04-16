"""Создает программно файл, записывает в него данные, вводимые пользователем"""
with open("task_1_text.txt", "w") as f_1:
    while True:
        content = input(f"Enter value to write in {f_1.name} or empty value to stop: ")
        f_1.write(content + "\n")
        if not content:
            break
