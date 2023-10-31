def score(x, y):
    points = 0
    if x**2 + y**2 <= 1:
        points = 10
    elif x**2 + y**2 <= 5**2:
        points = 5
    elif x**2 + y**2 <= 10**2:
        points = 1
    else:
        points = 0
    return points
