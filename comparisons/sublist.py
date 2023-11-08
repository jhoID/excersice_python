# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    list_one = "".join(str(number) + ", " for number in list_one)
    list_two = "".join(str(number) + ", " for number in list_two)

    if list_one == list_two:
        return EQUAL

    if list_two in list_one:
        return SUPERLIST

    if list_one in list_two:
        return SUBLIST

    return UNEQUAL