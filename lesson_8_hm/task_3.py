class OwnEx(Exception):
    def __init__(self, txt):
        self.txt = txt


some_list = []
while True:
    try:
        user_input = input("Enter a number or 'stop' to quit: ")
        if user_input == "stop":
            print(f"Result list: {some_list}")
            break
        if not user_input.isdigit():
            raise OwnEx("You entered not a number!")
    except OwnEx as err:
        print(err)
    else:
        user_input = int(user_input)
        some_list.append(user_input)
        print(f"Everything is OK. You entered {user_input}")
