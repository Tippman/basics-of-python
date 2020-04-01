revenue = int(input('Введите сумму выручки - '))
cost = int(input('Введите сумму издержек - '))

if revenue > cost:
    profit = revenue - cost
    print(f'Фирма получила прибыль: {profit}')
    effect = profit/revenue*100.3
    print(f'Рентабельность выручки: {effect:.2f} %')
    souls = int(input('Введите количество работников - '))
    print(f'Прибыль фирмы на одного работника: {profit/souls:.2f}')