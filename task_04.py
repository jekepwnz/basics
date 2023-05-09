def sort_list(list):
    if not list:
        return []
    minimum_value = min(list)
    maximum_value = max(list)

    min_indexes = []
    max_indexes = []
    for id, value in enumerate(list):
        if value == maximum_value:
            max_indexes.append(id)
        elif value == minimum_value:
            min_indexes.append(id)

    for index in min_indexes:
        list[index] = maximum_value

    for index in max_indexes:
        list[index] = minimum_value

    list.append(minimum_value)
    return list
