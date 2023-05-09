def multiply_numbers(inputs=[]):
    res = 1
    flag = False
    for elem in str(inputs):
        if elem.isdigit():
            res *= int(elem)
            flag = True
    if flag:
        return res
