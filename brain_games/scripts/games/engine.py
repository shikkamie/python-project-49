from brain_games.cli import welcome_user


def run_game(game_description, generate_question):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game_description)

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                "Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
