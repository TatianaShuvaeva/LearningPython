def rotate_word(word,n):
    result=""
    for c in word:  
        code = ord(c)
        new_code = ord(c) + number
        new_letter = chr(new_code)
        result += new_letter
    return result

word = 'cheer'
number = 7
new_word = rotate_word(word,number)
print(new_word)
   
