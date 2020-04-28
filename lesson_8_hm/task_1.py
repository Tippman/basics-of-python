class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date = input("Введите дату в формате '«день-месяц-год»'")
d_1 = Date.from_string(date)
is_date = Date.is_date_valid(date)
print("День", d_1.day, type(d_1.day))
print("Месяц", d_1.month, type(d_1.month))
print("Год", d_1.year, type(d_1.year))
print("Дата введена корректно" if is_date else "Дата введена некорректно")
