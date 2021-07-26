#!/usr/bin/env python3
import random
from brain_games.welcome import user_name


def calculate_answer():
    count_answer = 0
    print('What is the result of the expression?')
    while count_answer != 3:
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 10)
        num_operator = random.randint(1, 3)

        if num_operator == 1:
            print('Question: ' + str(num1) + ' + ' + str(num2))
            right_ans = num1 + num2
        elif num_operator == 2:
            print('Question: ' + str(num1) + ' * ' + str(num2))
            right_ans = num1 * num2
        else:
            print('Question: ' + str(num1) + ' - ' + str(num2))
            right_ans = num1 - num2
            answer = input()
        print('Your answer: ' + answer)
        if answer == str(right_ans):
            print('Correct!')
            count_answer += 1
        else:
            return (f"Sorry,'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{right_ans}'."
                    f"\n Let's try again, {user_name}!")
            break
    else:
        return 'Congratulations, ' + user_name + '!'
