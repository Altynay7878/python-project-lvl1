from random import randint, choice

game_rule = 'What is the result of the expression?'


def take_task_and_answer():
    rand_num1 = int(randint(0, 10))
    rand_num2 = int(randint(0, 10))
    operator = choice('+-*')
    task = str(f'{rand_num1}{operator}{rand_num2}')
    if operator == '+':
        correct_answer = str(rand_num1 + rand_num2)
    elif operator == '-':
        correct_answer = str(rand_num1 - rand_num2)
    elif operator == '*':
        correct_answer = str(rand_num1 * rand_num2)
    return task, correct_answer


def wrong_reply_calc():
    wrong_reply_calc = {' is wrong answer ;(. Correct answer was ', "'" + "." + '''Let's try again, '''}
    return wrong_reply_calc
