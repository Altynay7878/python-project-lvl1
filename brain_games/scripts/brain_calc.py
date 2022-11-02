import prompt
import random
from brain_games.cli_main import greeting, welcome_user
from brain_games.cli_calc import take_task_and_answer, game_rule

def main():
    greeting()
    name = prompt.string(welcome_user())
    print('Hello, ' + name + '!')
    print(game_rule)
    i = 0
    range = 3
    count = 0

    while i < range:
        answer, correct_answer = take_task_and_answer()
        print('Question: '+ answer + ' ')
        reply = prompt.string('Your answer: ')
        if reply == correct_answer:
            print('Correct!')
            i += 1
            count = count + 1
            if count == 3:
                result = print(f'Congratulations, {name}!')
                i = range
        else:
            result = print("'" + reply + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + correct_answer + "'" + "." + '''
Let's try again, ''' + name + '!')
            i = range
    return result


if __name__ == '__main__':
    main()
