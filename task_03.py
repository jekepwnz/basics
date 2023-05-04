def max_odd(arr):
    numbers = []
    for elem in arr:
        if isinstance(elem,(int, float)) and elem % 2 == 1:
            numbers.append(elem)
    return max(numbers) if numbers else None





print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd([1, 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None
