import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


user_name = welcome_user()