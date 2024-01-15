def count(number: int) -> int:
    if number == 2:
        return number

    new_value = number+1
   
    result = count(new_value)
    return result
     
    

new_value = count(1)
print(new_value)