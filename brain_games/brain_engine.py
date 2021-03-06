import prompt


NUMBER_OF_CORRECT_ANSWERS = 3


def run_engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))

    print(game.GAME_TASK)
    count_correct_answer = 1

    while count_correct_answer <= NUMBER_OF_CORRECT_ANSWERS:
        count_correct_answer += 1
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            print((f"'{answer}' is wrong answer ;(."
                   f"Correct answer was '{correct_answer}'"
                   f".\nLet's try again, {user_name}!"))
            break
    else:
        print(f'Congratulations, {user_name}!')
