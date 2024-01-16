def rotate_word(word,number):
    result = ""
    for c in word:  
        code = ord(c)
        new_code = get_new_code(number, code)
        new_letter = chr(new_code)
        result += new_letter
    return result

def get_new_code(number, code):
    new_code = code + number
    if chr(code).islower():
        if new_code > ord('z'):
            new_code -= 26
        if new_code < ord('a'):
            new_code += 26
        return new_code
    else:
        if new_code > ord('Z'):
            new_code -= 26
        if new_code < ord('A'):
            new_code += 26
        return new_code


word = 'KayAk'
number = 13
new_word = rotate_word(word,number)
print(new_word)


# assert rotate_word('cheer', 7) == 'jolly'
# assert rotate_word('CheER', 7) == 'JolLY'
# assert rotate_word('melon', -10) == 'cubed'
# assert rotate_word('mELoN', -10) == 'cUBeD'
# assert rotate_word('kayak', 13) == 'xnlnx'
# assert rotate_word('KaYAk', 13) == 'XnLNx'
