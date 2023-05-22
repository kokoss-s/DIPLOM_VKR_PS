PI = 3.14
ALLO = 2.5

COEF = {
    1: 1.2,
    2: 2.5,
    3: 0.9,
    4: 4,
}


def calculate_squere_first_ten(object_type):
    choice1_value = COEF[object_type]
    # if corner != 0:
    # squere_first_ten = round(0.5 * PI * ((0.5 * choice1_value * 10)**2))
    # else:
    squere_first_ten = round(PI * ((0.5 * choice1_value * 10)**2))
    return squere_first_ten
