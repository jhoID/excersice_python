def steps(number):
    number_steps = 0

    if number <= 0:
        raise ValueError("Only postive integers are allowed")

    while True:
        if number == 1:
            return number_steps

        number = number / 2 if number % 2 == 0 else number * 3 + 1

        number_steps += 1


print(steps(1))
