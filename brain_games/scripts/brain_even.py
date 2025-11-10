
from brain_games.scripts.games.engine import run_game
from brain_games.scripts.games.evens import description, generate_question

# старый код


# def find_even(name="Bill"):
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     count_answers = 0
#     while count_answers < 3:
#         number = random.randint(1, 100)
#         print(f"Question: {number}")
#         answer = input("Your answer: ")
#         if (number % 2 == 0 and answer == "yes") or (
#             number % 2 != 0 and answer == "no"
#         ):
#             print("Correct!")
#             count_answers += 1
#         else:
#             correct_answer = "yes" if number % 2 == 0 else "no"
#             print(
#                 f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
#             )
#             print(f"Let's try again, {name}!")
#             return

#     print(f"Congratulations, {name}!")


def main():
    # print("Welcome to the Brain Games!")
    # name = prompt.string("May I have your name? ")
    # print(f"Hello, {name}!")
    # find_even(name)
    run_game(description, generate_question)