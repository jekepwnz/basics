def coincidence(*args):
    result = []
    if len(args) == 2:
        result = [i for i in args[0] if i in args[1]]
    return result

def coincidence_2(list=[], range=0):
    result = [i for i in list if i in range]
    return result


