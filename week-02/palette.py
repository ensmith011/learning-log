import random
random.seed(5)

def make_color():
    r=(random.randint(0, 255 ))
    g=(random.randint(0, 255 ))
    b=(random.randint(0, 255 ))
    return r, g, b


def make_palette(count):
    for i in range(count):
        r, g, b = make_color()
        print("Color", i+1, r, g, b)


make_palette(4)
