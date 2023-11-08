def rebase(input_base, digits, output_base):
    # for input.
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # another example for input.
    if any(digit < 0 for digit in digits) or any(
        digit >= input_base for digit in digits
    ):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # or, for output.
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # passing to base 10
    base10_number = sum(
        digit * (input_base**index) for index, digit in enumerate(reversed(digits))
    )

    # passing to other bases different than 10
    tem_number = base10_number
    result_string = ""
    while tem_number // output_base != 0:
        result_string += str(tem_number % output_base)
        tem_number = tem_number // output_base
        if tem_number < output_base:
            result_string += str(tem_number)

    result_string = result_string[::-1]

    # returned digits
    result_digits = []

    if output_base == input_base:
        return digits

    if output_base == 10:
        string_number = str(base10_number)
        for number in string_number:
            result_digits.append(int(number))
    else:
        for number in result_string:
            result_digits.append(int(number))

    return result_digits


print(rebase(2, [1, 0, 1, 0, 1, 0], 10))
