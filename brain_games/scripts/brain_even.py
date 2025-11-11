from brain_games.scripts.games.engine import run_game
from brain_games.scripts.games.evens import description, generate_question


def main():
    # find_even(name)
    run_game(description, generate_question)
