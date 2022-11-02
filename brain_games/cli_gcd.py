import math
from random import randint

game_rule = 'Find the greatest common divisor of given numbers.'


def take_task_and_answer():
    rand_num1 = int(randint(0, 10))
    rand_num2 = int(randint(0, 10))
    task = str(f'{rand_num1} {rand_num2}')
    correct_answer = str(math.gcd(rand_num1, rand_num2))
    return task, correct_answer
