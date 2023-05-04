
def is_palindrome(string):
    no_symbols = []
    for char in str(string):
        if char.isalnum():
            no_symbols.append(char.lower())

    return no_symbols == no_symbols[::-1]


# print(is_palindrome("A man, a plan, a canal -- Panama"))# => True
# print(is_palindrome("Madam, I'm Adam!"))# => True
# print(is_palindrome(333)) # => True
# print(is_palindrome(None)) # => False
# print(is_palindrome("Abracadabra")) # => False