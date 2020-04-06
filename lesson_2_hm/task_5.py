my_list = [7, 5, 3, 3, 2]
user_input = int(input('Enter some number:'))
crnt_index = 0
for i, el in enumerate(my_list):
    if user_input > el:
        crnt_index = i
        break
    else:
        crnt_index = i + 1
my_list.insert(crnt_index, user_input)
print(my_list)
