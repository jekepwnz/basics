from re import sub
from string import punctuation as p

def count_words(string):
    string = sub(f'[{p}]',"", string)
    string = [word.strip().lower() for word in string.split()]
    result = {}

    for word in string:
        result[word] = result.get(word, 0) + 1

    print(result)

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}