def max_odd(arr):
    numbers = []
    for elem in arr:
        if isinstance(elem,(int, float)) and elem % 2 == 1:
            numbers.append(elem)
    if numbers:
        return max(numbers)
  #  return max(numbers) if numbers else None



