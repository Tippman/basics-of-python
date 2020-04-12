def multiple():
    """Выводит числа, кратные 20 и 21 из диапозона 20-240"""
    return [i for i in range(20, 241) if (i % 20 == 0 or i % 21 == 0)]