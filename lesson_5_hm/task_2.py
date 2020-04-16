"""В предварительно созданном файле выполняет подсчет строк и количесва слов в строке"""
lines_nbr = 0
total_words = 0
with open("task_2_text.txt") as f_2:
    for line in f_2:
        lines_nbr += 1
        total_words += len(line.split())
        print(f"Line № {lines_nbr}. Number of words per line: {len(line.split())}")
print(f"Total number of lines - {lines_nbr}, words in file - {total_words}")
