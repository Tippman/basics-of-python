from sys import argv

"""Расчитывает заработную плату по трем параметрам"""
scrip_name, time, cost, bonus = argv
time = int(time)
cost = int(cost)
bonus = int(bonus)
result = time * cost + bonus
print("Выработка в часах: ", time)
print("Ставка в час: ", cost)
print("Премия:  ", bonus)
print("-" * 40)
print("Заработная плата работника:", result)
print("-" * 40)