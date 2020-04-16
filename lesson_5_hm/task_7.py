import json

"""Выводит данные о прибыли фирмы из ранее созданного файла в словарь. Выводит данные в json"""
result_dict_firms = {}
firms_profit = 0
firms_in_profit_count = 0
with open("masha's_files/text_7.txt", encoding="utf-8") as f_7:
    for line in f_7:
        firm_name, firm_revenue, firm_costs = line.split()[0], int(line.split()[2]), int(line.split()[3])
        profit = firm_revenue - firm_costs
        if profit > 0:
            firms_profit += profit
            firms_in_profit_count += 1
        result_dict_firms[firm_name] = profit
    result = [result_dict_firms, {"average_profit": firms_profit / firms_in_profit_count}]
with open("task_7_json.json", "w", encoding="utf-8") as f_7_json:
    json.dump(result, f_7_json, indent=4, ensure_ascii=False)
print(result)
