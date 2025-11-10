from brain_games.scripts.games.engine import run_game
from brain_games.scripts.games.calc import description, generate_question


def main():
    run_game(description, generate_question)


