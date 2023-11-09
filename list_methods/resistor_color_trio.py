COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def label(colors):
    index1 = COLORS.index(colors[0])
    index2 = COLORS.index(colors[1])
    index3 = COLORS.index(colors[2])
    ohms = 1 if index3 == 0 else 10**index3
    value = (index1 * 10 + index2) * ohms
    if value == 0:
        return "0 ohms"
    elif value % (10**9) == 0:
        return f"{value//(10**9)} gigaohms"
    elif value % (10**6) == 0:
        return f"{value//(10**6)} megaohms"
    elif value % (10**3) == 0:
        return f"{value//(10**3)} kiloohms"
    else:
        return f"{value} ohms"
