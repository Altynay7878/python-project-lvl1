import prompt
import random
from brain_games.cli_main import greeting, welcome_user

def main():
    greeting()
    name = input(welcome_user())
    print('Hello, ' + name + '!')
    print('''Answer "yes" if the number is even, otherwise answer "no".''')
    i = 0
    range = 3
    count = 0

    while i < 3:
        num = random.randint(0, 100)
        print('Question: ' + str(num) + ' ')
        reply = prompt.string('Your answer: ')
        if (num % 2 == 0 and reply == 'yes') or (num % 2 != 0 and reply == 'no'):
            result = print('Correct!')
            count += 1
        elif (num % 2 == 0 and reply != 'yes'):
            result = print("'" + reply + "'" + ''' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, ''' + name + '!')
            i = 3
        elif num % 2 != 0 and reply != 'no':
            result = print("'" + reply + "'" + ''' is wrong answer ;(. Correct answer was 'no'.
Let's try again, ''' + name + '!')
            i = 3
        i += 1
        if count == 3:
            result = print('Congratulations, ' + name + '!')
    return result


if __name__ == '__main__':
    main()
