# Python Assignment-03

# Check whether a triangle is right-angled


def is_right_angled(a, b, c):
    # Arrange the sides so that the largest side is last
    sides = sorted([a, b, c])

    # Pythagorean theorem:
    # a² + b² = c²

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    else:
        return False


# Take input from user
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))


# Check the triangle
if is_right_angled(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")