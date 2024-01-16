def rotate_word(word,number):
    result=""
    for c in word:  
        code = ord(c)
        new_code = code + number
        if new_code > ord('z'):
            new_code -= 26
        if new_code < ord('a'):
            new_code += 26
        new_letter = chr(new_code)
        result += new_letter
    return result

word = 'kayak'
number = 13
new_word = rotate_word(word,number)
print(new_word)


assert rotate_word('cheer', 7) == 'jolly'
assert rotate_word('melon', -10) == 'cubed'
assert rotate_word('kayak', 13) == 'xnlnx'
