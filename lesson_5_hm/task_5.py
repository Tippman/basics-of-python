from random import randint

"""Создает текстовый файл и записывает в него 50 произвольных чисел"""

numbers = [randint(0, 1000) for i in range(50)]

with open("task_5_text.txt", "w", encoding="utf-8") as f_5:
    f_5.write(" ".join(str(j) for j in numbers))
print(f"Сумма чисел, записанных в файл {f_5.name} равна {sum(numbers)}")
