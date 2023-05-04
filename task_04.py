def sort_list(list):
    if not list:
        return []
    min = float('+inf')
    max = float('-inf')
    for elem in list:     # масимальное и минимальное значение
        if elem > max:
            max = elem
        if elem < min:
            min = elem
    min_indexes = []
    max_indexes = []
    for id, value in enumerate(list):   # индексы максимальных и минимальных значений
        if value == max:
            max_indexes.append(id)
        elif value == min:
            min_indexes.append(id)

    for index in min_indexes:
        list[index] = max
    for index in max_indexes:
        list[index] = min
    list.append(min)
    return list


print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]