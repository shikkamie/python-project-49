import random

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():

    num = random.randint(1, 100)
    correct_answer = "yes"
    if num <= 1:
        correct_answer = "no"
    if num == 2:
        correct_answer = "yes"
    if num % 2 == 0:
        correct_answer = "no"
    for i in range(3, int(num**0.5), 2):
        if num % i == 0:
            correct_answer = "no"

    return str(num), correct_answer
