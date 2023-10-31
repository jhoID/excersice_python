def is_triangle(sides):
    result = False
    a, b, c = sorted(sides)

    flag1 = a + b >= c
    flag2 = b + c >= a
    flag3 = a + c >= b

    if flag1 and flag2 and flag3:
        result = True

    return result


def is_triangle_v2(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        raise ValueError("sides can't be 0")
    return abs(a - b) < c < a + b

# print(is_triangle_v2([3, 4, 5]))

# my variable test
sides = [1, 1, 3]


def equilateral(sides):
    if not is_triangle_v2(sides):
        raise ValueError("The sides are wrong")

    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_triangle_v2(sides):
        raise ValueError("The sides are wrong")

    if equilateral(sides):
        return True

    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if isosceles(sides):
        return False
    if equilateral(sides):
        return False

    return True


print(equilateral(sides))
print(isosceles(sides))
print(scalene(sides))