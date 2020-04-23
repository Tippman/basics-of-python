class Mesh:
    """Выполняет перегрузки орифметических оператов с ячейками"""
    def __init__(self, nmbr_cells):
        self.nmbr_cells = nmbr_cells

    def __add__(self, other):
        return f"Результат сложения: {self.nmbr_cells + other.nmbr_cells}"

    def __sub__(self, other):
        return f"Результат вычетания: {self.nmbr_cells - other.nmbr_cells}" \
            if self.nmbr_cells - other.nmbr_cells >= 0 \
            else "Вычетание ячеек не может быть отрицательным числом"

    def __mul__(self, other):
        return f"Результат умножения: {self.nmbr_cells * other.nmbr_cells}"

    def __truediv__(self, other):
        return f"Результат деления: {self.nmbr_cells // other.nmbr_cells}" \
            if self.nmbr_cells // other.nmbr_cells > 0 \
            else "Ячейки могут делиться только нацело"

    def make_order(self, cells_in_row):
        return ("*" * cells_in_row + "\n") * (self.nmbr_cells // cells_in_row) + "*" * (self.nmbr_cells % cells_in_row)


c_1 = Mesh(12)
c_2 = Mesh(11)
c_3 = Mesh(15)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 - c_3)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1 / c_3)
print(c_1.make_order(7))
