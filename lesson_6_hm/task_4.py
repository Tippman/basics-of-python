from random import choice

"""Создает несколько типов авто"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")

    def go(self):
        print(f"The car {self.name} went")

    def stop(self):
        print(f"The car {self.name} stopped")

    def turn(self):
        directions = ["East", "West", "North", "South"]
        print(f"The car {self.name} turned {choice(directions)}")

    def is_it_police(self):
        print(
            f"The car {self.name} is not police" if not self.is_police else f"Attention! The car {self.name} is police!")


class TownCar(Car):
    def show_speed(self):
        print(
            f"Current speed of car {self.name} is {self.speed}. Attention! The speed limit 60 is exceeded on {self.speed - 60}" if self.speed > 60 else f"current speed of car {self.name} is {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(
            f"Current speed of car {self.name} is {self.speed}. Attention! The speed limit 40 is exceeded on {self.speed - 40}" if self.speed > 40 else f"current speed of car {self.name} is {self.speed}")


class PoliceCar(Car):
    pass


c_town = TownCar(83, "black", "Tyoyta", False)
c_sport = SportCar(160, "red", "Ferrari", False)
c_work = WorkCar(65, "white", "Mercedes", False)
c_cop = PoliceCar(40, "white-blue", "BMW", True)

c_town.go()
c_town.is_it_police()
c_town.show_speed()
c_town.turn()
c_town.stop()
print("-" * 30)

c_sport.go()
c_sport.is_it_police()
c_sport.show_speed()
c_sport.turn()
c_sport.stop()
print("-" * 30)

c_work.go()
c_work.is_it_police()
c_work.show_speed()
c_work.turn()
c_work.stop()
print("-" * 30)

c_cop.go()
c_cop.is_it_police()
c_cop.show_speed()
c_cop.turn()
c_cop.stop()
