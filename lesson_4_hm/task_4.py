def non_repeat(some_list):
    """Выводит не повторяющиеся элементы списка"""
    return [i for i in some_list if some_list.count(i) == 1]