user_input = input('Enter some words: ')
for i, el in enumerate(user_input.split(' ')):
    print(i + 1, el if len(el) <= 10 else el[:10])
