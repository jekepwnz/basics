def keygen(dict):
    return(dict)

def connect_dicts(dict1, dict2):
    if sum(dict1.values()) > sum(dict2.values()):
        dict1, dict2 = dict2, dict1
    res_dict = {}
    for k, v in dict1.items():
        if v >= 10:
            res_dict[k] = v
    for k, v in dict2.items():
        if v >= 10:
            res_dict[k] = v

    return dict(sorted(res_dict.items(), reverse=True))


print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }