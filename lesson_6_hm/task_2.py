"""Расчет массы асфальта (единицы измерения в метрах и тоннах"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass_per_cubic = 2.5
        depth = 0.05
        result_mass = self._length * self._width * depth * mass_per_cubic
        return result_mass


road_1 = Road(5000, 20)
print(f"Необходимая масса асфальта {road_1.mass()}")
