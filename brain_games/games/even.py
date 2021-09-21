from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDINT = 1
MAX_RANDINT = 100


def is_even(num):
    return num % 2 == 0


def question_and_answer():
    question = randint(MIN_RANDINT, MAX_RANDINT)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
