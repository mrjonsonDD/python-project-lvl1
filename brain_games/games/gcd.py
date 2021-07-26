import random
import math
from brain_games.welcome import user_name


def greatest_common_divisor():
    count_answer = 0
    print('Find the greatest common divisor of given numbers.')
    while count_answer != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print('Question: ' + str(num1) + ' ' + str(num2))
        greatest_divisor = math.gcd(num1, num2)
        answer = input()
        print('Your answer: ' + answer)
        if answer == str(greatest_divisor):
            print('Correct!')
            count_answer += 1
        else:
            return (f"Sorry,'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{greatest_divisor}'."
                    f"\n Let's try again, {user_name}!")

    else:
        return 'Congratulations, ' + user_name + '!'
