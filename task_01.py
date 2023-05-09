
def is_palindrome(string):
    no_symbols = []
    for char in str(string):
        if char.isalnum():
            no_symbols.append(char.lower())

    return no_symbols == no_symbols[::-1]

