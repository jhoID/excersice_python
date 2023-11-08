def rebase(input_base, digits, output_base):

    # convert to base 10 number
    string_number = str(digits)
    index = len(string_number) - 1
    suma = 0
    for number in string_number:
        suma += int(number) * (input_base**index)
        index -= 1

    if output_base == 10:
        return suma

    if input_base == output_base:
        return digits

    # conver to output_base
    final_change = ""
    quotient = suma
    while quotient // output_base != 0:
        final_change += str(quotient % output_base)
        quotient = quotient // output_base
        if quotient < output_base:
            final_change += str(quotient)

    return int(final_change[::-1])

print(rebase(10, 42, 3))