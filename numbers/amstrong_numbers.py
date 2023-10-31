def is_armstrong_number(number):
    num_temp = number
    digits = []
    count = 0
    while num_temp > 0:
        digit = num_temp%10
        num_temp = num_temp//10
        digits.append(digit)
        count+=1

    suma = 0

    for i in range(count):
        suma += digits[i]**count
    
    if suma == number:
        return True
    
    return False
    

print(is_armstrong_number(12))

# print(123%10)
# print(1//10)
