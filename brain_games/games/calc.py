from random import randint

GAME_TASK = 'What is the result of the expression?'
MIN_FIRST_RANDINT = 10
MAX_FIRST_RANDINT = 20
MIN_SECOND_RANDINT = 1
MAX_SECOND_RANDINT = 10


def get_operator(num1, num2):
    num_operator = randint(1, 3)
    if num_operator == 1:
        operator = ' + '
        right_ans = num1 + num2
    elif num_operator == 2:
        operator = ' * '
        right_ans = num1 * num2
    else:
        operator = ' - '
        right_ans = num1 - num2
    return str(right_ans), operator


def question_and_answer():
    num1 = randint(MIN_FIRST_RANDINT, MAX_FIRST_RANDINT)
    num2 = randint(MIN_SECOND_RANDINT, MAX_SECOND_RANDINT)
    correct_answer, operator = get_operator(num1, num2)
    question = '{} {} {}'.format(num1, operator, num2)
    return question, correct_answer
