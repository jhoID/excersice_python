def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors_sum = 0
    divider = 1
    while divider <= number / 2:
        if number % divider == 0:
            factors_sum += divider
        divider += 1

    if factors_sum < number:
        return "deficient"
    elif factors_sum > number:
        return "abundant"
    else:
        return "perfect"
