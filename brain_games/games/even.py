import random
from brain_games.welcome import user_name


def even_number():
    count_answer = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_answer != 3:
        num = random.randint(1, 100)
        if num % 2 == 0:
            corr_ans = "'yes'"
        else:
            corr_ans = "'no'"
            print('Question:' + str(num))
            answer = input()
            print('Your answer: ' + answer)
        if answer == 'yes' and num % 2 == 0 or answer == 'no' and num % 2 != 0:
            print('Correct!')
            count_answer += 1
        else:
            return (f"Sorry,'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{corr_ans}'."
                    f"\n Let's try again, {user_name}!")

    else:
        return 'Congratulations, ' + user_name + '!'
