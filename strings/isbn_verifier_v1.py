def is_valid(isbn):
    result = False
    if isbn == "":
        return False

    if len(isbn.replace("-", "")) != 10:
        return False

    if not isbn[-1].isdigit() and isbn[-1] != "X":
        return False
    
    nums = [int(elemento) for elemento in isbn if elemento.isdigit()]

    suma = 0
    weight = 10

    if "X" in isbn:
        nums.append(10)

    print(len(nums))

    if len(nums) < 10:
        return False

    for i in nums:
        suma += i * weight
        weight -= 1

    if suma % 11 == 0:
        result = True

    return result
