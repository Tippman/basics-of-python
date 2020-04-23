from abc import ABC, abstractmethod


class Cloth(ABC):
    """Определяет расход ткани в зависимости от типа одежды"""
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    @property
    def prop(self):
        return f"Параметры, переданные в класс:\n" \
               f"Наименование: {self.name}, размер/рост: {self.param}"

    def __str__(self):
        prnt = f"\nДля одежды {self.name} расход ткани: {self.consumption()}\n"
        return self.prop + prnt + "-" * 40


class Coat(Cloth):
    def consumption(self):
        return round(self.param / 6.5 + 0.5, 2)
    pass


class Costume(Cloth):
    def consumption(self):
        return self.param * 2 + 0.3


cl_1 = Coat('Конское пальто', 78)
cl_2 = Coat("GUCCI", 36)
cl_3 = Costume('Catcharel', 178)
print(cl_1)
print(cl_2)
print(cl_3)
