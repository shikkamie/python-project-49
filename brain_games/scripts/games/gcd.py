import random

description = "Find the greatest common divisor of given numbers"


def generate_question():

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    a_1 = a
    b_1 = b
    result = 0
    if b == 0:
        result = a
    else:
        while b != 0:
            a, b = b, a % b
            if b == 0:
                result = a

    return f"{a_1} {b_1}", str(result)
