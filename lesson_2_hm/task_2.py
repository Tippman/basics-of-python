list_1 = input('enter list 1: ')
list_1 = list(list_1)
list_result = []
j = 0

for i in range(int(len(list_1) / 2)):
    list_result.append(list_1[j + 1])
    list_result.append(list_1[j])
    j += 2
if len(list_1) % 2 != 0:
    list_result.append(list_1[-1])

print(list_result)
