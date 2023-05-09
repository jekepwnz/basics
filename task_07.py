def combine_anagrams(words_array):
    preres_dict = {}
    for word in words_array:
        sorted_word = "".join(sorted(word.lower()))
        preres_dict.setdefault(sorted_word, []).append(word)
    res = [value for value in preres_dict.values()]

    return res


print(combine_anagrams(["cars", "fOr", "potatoes", "rAcs", "four", "scar",
                        "creams", "scream"]))