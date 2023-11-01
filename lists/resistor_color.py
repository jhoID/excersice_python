COLORS = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]

def color_code(color):
    colors = [color.lower() for color in COLORS  ]
    return COLORS.index(color)


def colors():
    return COLORS
