from random import randint

game_rule = 'What number is missing in the progression?'


def take_task_and_answer():
    start = randint(2, 10)
    step = int(randint(2, 7))
    stop = int(start) + 10 * step
    progression = []
    for i in range(start, stop, step):
        progression.append(str(i))
    length = len(progression) - 1
    index = randint(1, length)
    correct_answer = progression[index]
    progression[index] = '..'
    task = " ".join(map(str, progression))
    return task, correct_answer
