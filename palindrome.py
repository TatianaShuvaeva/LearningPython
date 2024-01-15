# def first(word):
#     return word[0]

# def last(word):
#     return word[-1]

# def middle(word):   
#     return word[1:-1]
    
# word = 'Klavier'
# print(middle(word))

def is_palidrome(word):
    if word == word[::-1]:
        return True
    else:
        return False



print(is_palidrome('kayak'))


