import re

"""Выводит словарь с ключом - название предмета и значением - сумма часов"""
result = {}
with open("masha's_files/text_6.txt", encoding="utf-8") as f_6:
    for line in f_6:
        result[line.split(": ")[0]] = sum([int(j) for j in re.findall(r"\w+", line.split(": ")[1]) if j.isdigit()])
print(result)
