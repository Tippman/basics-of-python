"""Вывод полного имени работника и дохода"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя работника: {self.name + ' ' + self.surname}")

    def get_total_income(self):
        try:
            print(f"Доход с учетом премии: {int(self._income['wage'] + self._income['bonus'])}\n")
        except (TypeError, ValueError):
            print("Доход с учетом премии: Данные введены некорректно")


worker_1 = Position("Vasya", "Pupkin", "senior assistant", 100000, 20000)
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position("Владимир", "Путин", "Президент", "not available", "not available")
worker_2.get_full_name()
worker_2.get_total_income()
