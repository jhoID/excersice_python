def is_valid(isbn):
    result = False
    
    if len(isbn.replace('-', '')) != 10 or isbn=='' or (not isbn[-1].isdigit() and  isbn[-1] != 'X'):
        return False
    
    nums = [int(elemento) if elemento != 'X' and elemento.isdigit() else 10 for elemento in isbn]

    suma = 0
    weight = 10

    for i in nums:
        suma += i * weight
        weight -= 1

    if suma % 11 == 0:
        result = True
    return result