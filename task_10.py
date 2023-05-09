from re import sub
from string import punctuation as p

def count_words(string):
    string = sub(f'[{p}]',"", string)
    string = [word.strip().lower() for word in string.split()]
    result = {}

    for word in string:
        result[word] = result.get(word, 0) + 1

    print(result)
