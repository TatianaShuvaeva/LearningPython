def rotate_word(word,n):
    result=""
    for c in word:  
        code = ord(c)
        new_code = ord(c) + number
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
   
