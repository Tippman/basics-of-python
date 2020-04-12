from random import randint
from functools import reduce
from task_2 import compare
from task_3 import multiple
from task_4 import non_repeat
from task_6 import rnd_nmb_from, cycle_from_list
from task_7 import factorial

"""_TASK 2_"""
some_list = [randint(1, 300) for i in range(1, 20)]
print("-" * 60, "\nЗадача 2")
print("Исходный список: ", some_list)
print("Отсортированный список: ", compare(some_list))

"""_TASK 3_"""
print("-" * 60, "\nЗадача 3")
print("Для чисел в пределах от 20 до 240, кратные 20 или 21 следующие:\n", multiple())

"""_TASK 4_"""
print("-" * 60, "\nЗадача 4")
print("Исходный список: ", [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
print("Элементы списка, не имеющие повторений: ", non_repeat([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))

"""_TASK 5_"""
print("-" * 60, "\nЗадача 5")
print("Произведение четных чисел из списка от 100 до 1000:",
      reduce(lambda a, b: a * b, [i for i in range(100, 1001) if i % 2 == 0]))

"""_TASK 6_"""
print("-" * 60, "\nЗадача 6")
print("а) итератор, генерирующий целые числа, начиная с 4 до 20:", rnd_nmb_from(3))
print("b) итератор, повторяющий элементы строки 15 раз (вывод в виде списка): ", cycle_from_list("qwerty", 15))

"""_TASK 7_"""
print("-" * 60, "\nЗадача 7")
print("Получение факториала числа N с помощью yield: ")
for el in factorial(12):
    print(el)
