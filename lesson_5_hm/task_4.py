"""Переводит английские числительные из одного файла на русский и записывает результат в новый файл."""
translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Zero": "ноль",
}

with open("task_4_text.txt", "w", encoding="utf-8") as f_result:
    with open("masha's_files/text_4.txt", encoding="utf-8") as f_4:
        for line in f_4:
            key = line.split(" - ")[0]
            try:
                line_to_result = " - ".join([translate.get(key), line.split(" - ")[1]])
                f_result.write(line_to_result)
            except TypeError:
                print(f"Value '{key}' does not exist in dictionary")
print(f"Text translate from {f_4.name} has been done in {f_result.name}")
