days = 1
start_dist = int(input('Введите результат первого дня пробежки в км - '))
get_dist = int(input('Введите необходимую дистанцию - '))
result = start_dist

while result < get_dist:
    result *= 1.1
    days += 1
print(f'На {days}-й день спортсмен достигнет результата - не менее {get_dist} км')
