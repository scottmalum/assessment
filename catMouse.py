# Cat and Mouse Challenge
def catAndMouse(x, y, z):
    A = abs(z-x)
    B = abs(z-y)
    if A>B:
        return str("Cat B")
    elif A<B:
        return str("Cat A")
    else:
        return str("Mouse C")





