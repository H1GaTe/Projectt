import random

random_number = random.randint(1, 5)
user_number = input('Угадай число(от 1 до 5):')

if user_number == random_number:
    print('Вы угадали!')
    print('123')
else:
    print('Вы не угадали :(')
    print(f'Было загадано число {random_number}')


input()