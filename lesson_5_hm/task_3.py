"""Выводит фамилии работников с з/п менее 20000 из предварительно созданного файла"""
total_salary = 0
workers = 0
print("Сотрудники с з/п менее 20 тыс:")
with open("masha's_files/text_3.txt", encoding="utf-8") as f_3:
    for line in f_3:
        workers += 1
        total_salary += float(line.split()[1])
        print(line.split()[0]) if float(line.split()[1]) < 20000 else False
print("Средняя з/п: ", total_salary / workers)
