import time

"""Светофор. Время работы программы 30 сек"""


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self, delay):
        print(f"\rNow is {self.__color} light", end="")
        for i in range(1, delay + 1):
            time.sleep(1)
            print(f"...{i}...", end="")


time_end = time.time() + 30
while time.time() < time_end:
    red = TrafficLight('red')
    red.running(7)
    yel = TrafficLight('yellow')
    yel.running(2)
    green = TrafficLight('green')
    green.running(5)
    yel = TrafficLight('yellow')
    yel.running(2)
