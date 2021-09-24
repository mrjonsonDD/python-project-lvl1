from random import randint, randrange

GAME_TASK = 'What number is missing in the progression?'
MIN_RANDINT = 1
MAX_RANDINT = 100
MIN_FOR_STEP = 1
MAX_FOR_STEP = 10


def mysterious_proggression(start_num, end_num, step, correct_answer):
    mysterious_prog = ''
    for item in range(start_num, end_num, step):
        if item != correct_answer:
            mysterious_prog += str(item) + ' '
        else:
            mysterious_prog += '.. '
    return mysterious_prog


def question_and_answer():
    start_num = randint(MIN_RANDINT, MAX_RANDINT)
    step = randint(MIN_FOR_STEP, MAX_FOR_STEP)
    end_num = start_num + 4 * step + 1
    correct_answer = randrange(start_num, end_num + 1, step)
    question = mysterious_proggression(start_num, end_num, step, correct_answer)
    return question, str(correct_answer)
