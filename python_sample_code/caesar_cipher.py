alpha = "abcdefghijklmnopqrstuvwxyz"
input_string = "Why hello there! How goes it?"

def shift_char(input_char, shift, alpha):
    upper = False
    if input_char.isupper():
        upper = True
        input_char = input_char.lower()
    if input_char in alpha: # character in alpha
        new_position = (alpha.index(input_char) + shift) % len(alpha)
        input_char = alpha[new_position]
        if upper: #if it used to be uppercase
            return input_char.upper()
        return input_char
    else: # character not in alphabet, leave it alone
        return input_char

def caesar(input_string, shift, alpha):
    new_string = ""
    for i in input_string:
        new_string += shift_char(i, shift, alpha)
    return new_string

print(caesar(input_string, 25, alpha))

