from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDINT = 1
MAX_RANDINT = 100
FIRST_PRIME = 2


def is_prime(num):
    if num < FIRST_PRIME:
        return False

    for item in range(FIRST_PRIME, num // 2 + 1):
        if num % item == 0:
            return False
    return True


def question_and_answer():
    question = randint(MIN_RANDINT, MAX_RANDINT)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
