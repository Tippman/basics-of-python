def compare(some_list):
    """Сортирует список, извлекает только числа, которые больше предыдущих"""
    result = [i for i in some_list if i > some_list[some_list.index(i) - 1]]
    result.pop(0)
    return result