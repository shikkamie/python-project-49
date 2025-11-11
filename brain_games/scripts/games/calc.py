import random

description = "What is the result of the expression?"


def generate_question():
    operator = random.choice(["+", "-"])
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    if operator == "-" and a < b:
        a, b = b, a

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b

    return f"{a} {operator} {b}", str(result)
