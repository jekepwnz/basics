def multiply_numbers(inputs=[]):
    res = 1
    flag = False
    for elem in str(inputs):
        if elem.isdigit():
            res *= int(elem)
            flag = True
    return res if flag else None




print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120