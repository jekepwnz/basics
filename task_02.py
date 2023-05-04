def coincidence(*args):
    result = []
    if len(args) == 2:
        result = [i for i in args[0] if i in args[1]]
    return result

def coincidence_2(list=[], range=0):
    result = [i for i in list if i in range]
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence())    # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]

print()

print(coincidence_2([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence_2())    # => []
print(coincidence_2([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]
