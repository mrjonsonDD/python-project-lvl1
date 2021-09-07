from random import randint
import math


GAME_TASK = 'Find the greatest common divisor of given numbers.'
MIN_RANDINT = 1
MAX_RANDINT = 100


def question_and_answer():
    num1 = randint(MIN_RANDINT, MAX_RANDINT)
    num2 = randint(MIN_RANDINT, MAX_RANDINT)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
