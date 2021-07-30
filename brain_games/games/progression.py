import random
from brain_games.welcome import user_name


def arithmetic_progression():
    count_answer = 0
    print('What number is missing in the progression?')
    while count_answer != 3:
        start_num = random.randint(1, 100)
        step = random.randint(1, 10)
        end_num = start_num + 4 * step + 1
        mysterious_num = random.randrange(start_num, end_num + 1, step)
        mysterious_prog = ''
        for i in range(start_num, end_num, step):
            if i != mysterious_num:
                mysterious_prog += ' ' + str(i)
            else:
                correct = mysterious_prog
                mysterious_prog += ' ..'
        print('Question: ' + mysterious_prog)
        answer = input()
        print('Your answer: ' + answer)
        correct = str(mysterious_num)
        if answer == correct:
            print('Correct!')
            count_answer += 1
        else:
            return (f"Sorry,'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct}'."
                    f"\n Let's try again, {user_name}!")
            break

    else:
        return 'Congratulations, ' + user_name + '!'
