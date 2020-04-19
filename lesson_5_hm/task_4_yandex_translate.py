import requests
import json

"""Переводит с английского на русский файл, результат записывается в новый файл.
Должен быть установлен модуль requests.
"""
token = "trnsl.1.1.20200416T132512Z.0bdb58c00f70557b.b1aec4ed1dc72e76cc6c08980f7ed0c2de92ae86"
url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

with open("task_4_text_yandex.txt", "w", encoding="utf-8") as f_result:
    with open("masha's_files/text_4.txt", encoding="utf-8") as f_4:
        for line in f_4:
            eng_text = line
            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params=trans_option)
            trans_dict = json.loads(webRequest.text)
            line_to_result = "".join(trans_dict["text"])
            f_result.write(line_to_result)

print(f"Text translate from {f_4.name} has been done in {f_result.name}")
