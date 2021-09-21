from random import randint
import math


GAME_TASK = 'Find the greatest common divisor of given numbers.'
MIN_RANDINT = 1
MAX_RANDINT = 100


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def question_and_answer():
    num1 = randint(MIN_RANDINT, MAX_RANDINT)
    num2 = randint(MIN_RANDINT, MAX_RANDINT)
    question = f'{num1} {num2}'
    correct_answer = str(get_gcd(num1, num2))
    return question, correct_answer
