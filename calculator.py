num1 = float(input('enter your first number: '))
operator = input('enter operator: ')
num2 = float(input('enter your second number: '))

def error_prompt():
    print('invalid operator')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    error_prompt()
