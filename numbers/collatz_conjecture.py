def steps(number):
    num_steps = 0
    temp_number = number

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while True:
        if temp_number == 1:
            return num_steps

        if temp_number % 2 == 0:
            temp_number = temp_number / 2
        else:
            temp_number = 3 * temp_number + 1

        num_steps += 1


print(steps(-2))
