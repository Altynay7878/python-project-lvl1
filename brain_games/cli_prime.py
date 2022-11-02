import math
from random import randint, random

game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def take_task_and_answer():
    task = randint(0, 100)
    if task > 1:
        for i in [2, task]:
            if task % i == 0:
                correct_answer = "no"
            else:
                correct_answer = "yes"
    else:
        correct_answer = "no"
    return task, correct_answer