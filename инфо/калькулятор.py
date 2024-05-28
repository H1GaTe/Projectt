from colorama import init 
from colorama import Fore, Back, Style
init()

print(Fore.LIGHTBLACK_EX)

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

print(Fore.GREEN)

operation = input("Что сделать? (+, -, *, /): ")

if operation == '+':
    result = a + b
elif  operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b

print(Fore.LIGHTYELLOW_EX)

print(f'Результат: {result}')

input()