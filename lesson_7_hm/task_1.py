from copy import deepcopy


class Matrix:
    """Выполняет сложение нескольких матриц одинаковой разрядности"""
    def __init__(self, matr):
        self.matr = matr
        self.res = deepcopy(self.matr)

    def __str__(self):
        self.view_m = '\n'.join(
            ['\t'.join(
                [str(i) for i in j]) for j in self.matr])
        return self.view_m

    def __add__(self, other):
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                self.res[i][j] = self.matr[i][j] + other.matr[i][j]
        return Matrix(self.res)


m_1 = Matrix([[1, 2, 3], [0, 2, 5], [4, 6, 7]])
m_2 = Matrix([[5, 6, 7], [3, 9, 0], [8, 1, 2]])
print(m_1 + m_2)
