import random
from brain_games.welcome import user_name


def prime_number():
    count_answer = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count_answer != 3:
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = input()
        print('Your answer: ' + answer)
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k = k + 1
        if k <= 0:
            corr_ans = "'yes'"
        else:
            corr_ans = "'no'"
        if answer == 'yes' and k <= 0 or answer == 'no' and k >= 0:
            print('Correct!')
            count_answer += 1
        else:
            return (f"Sorry,'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{corr_ans}'."
                    f"\n Let's try again, {user_name}!")
    else:
        return 'Congratulations, ' + user_name + '!'
