class OwnEx(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        inp_num = input("Enter a nominator or 'stop' to quit: ")
        if inp_num == "stop":
            print("You stopped the program")
            break
        inp_denom = input("Enter a denominator or 'stop' to quit: ")
        if inp_denom == "stop":
            print("You stopped the program")
            break
        inp_num = int(inp_num)
        inp_denom = int(inp_denom)
        if inp_denom == 0:
            raise OwnEx("You can't divide by zero!")
    except ValueError:
        print("You entered not a number!")
    except OwnEx as err:
        print(err)
    else:
        print(f"Result of the division: {round(inp_num / inp_denom, 2)}")
