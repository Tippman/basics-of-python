print("Заполните структуру данных:")
user_count = int(input("Введите количество товаров, которое необходимо ввести - "))
result_list = []
name_list = []
cost_list = []
count_list = []
units_list = []
result_dict = {}
for i in range(user_count):
    item_name = input(f'Введите название товара № {i + 1} - ')
    item_cost = int(input(f'Ввидте стоимость товара "{item_name}" - '))
    item_count = int(input(f'Ввидте количество товара "{item_name}" - '))
    units = input(f'Ввидте единицы измерения количества товара "{item_name}" - ')
    temp_dict = {
        "название": item_name,
        "цена": item_cost,
        "количество": item_count,
        "ед": units
    }
    result_list.append(tuple((i + 1, temp_dict)))
    name_list.append(item_name)
    cost_list.append(item_cost)
    count_list.append(item_count)
    units_list.append(units)

print('\nИтоговый перечень товаров:')
for i in result_list:
    print(i)

dict2 = {
    "название": name_list,
    "цена": cost_list,
    "количество": count_list,
    "ед": set(units_list)
}
print(f'\nАналитика товаров:\n {dict2}')