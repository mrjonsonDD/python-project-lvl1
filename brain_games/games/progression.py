from random import randint, randrange

GAME_TASK = 'What number is missing in the progression?'
MIN_RANDINT = 1
MAX_RANDINT = 100
MIN_FOR_STEP = 1
MAX_FOR_STEP = 10


def mysterious_proggression(start_num, end_num, step):
    mysterious_num = randrange(start_num, end_num + 1, step)
    mysterious_prog = ''
    for index in range(start_num, end_num, step):
        if index != mysterious_num:
            mysterious_prog += str(index) + ' '
        else:
            mysterious_prog += '.. '
    return mysterious_prog, mysterious_num


def question_and_answer():
    start_num = randint(MIN_RANDINT, MAX_RANDINT)
    step = randint(MIN_FOR_STEP, MAX_FOR_STEP)
    end_num = start_num + 4 * step + 1
    question, correct_answer = mysterious_proggression(start_num, end_num, step)
    return question, str(correct_answer)
