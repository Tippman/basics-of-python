class ComplexNmbrs:
    def __init__(self, comp_num):
        self.comp_num = comp_num

    def __add__(self, other):
        return self.comp_num + other.comp_num

    def __mul__(self, other):
        return self.comp_num * other.comp_num


c_n_1 = ComplexNmbrs(1 + 3j)
c_n_2 = ComplexNmbrs(2 + 2j)
print(c_n_1 + c_n_2)
print(c_n_1 * c_n_2)
