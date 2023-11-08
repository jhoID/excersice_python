def rebase(input_base, digits, output_base):
    output_digits = []
    
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

    base10_number = sum(
        digit * input_base**index for index, digit in enumerate(reversed(digits))
    )

    if base10_number == 0:
        return [0]

    while base10_number != 0:
        output_digits.insert(0, base10_number%output_base)
        base10_number = base10_number//output_base

    return output_digits
