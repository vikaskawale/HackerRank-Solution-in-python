

num1 = float(input('Enter first number: '))
operator = input('which operation to perform (+, -, *, /): ')
num2 = float(input('Enter second number: '))

result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print('Answer: ', result)


nextOpeation = input('Do you want to perform more opration in this calculation: (y, n): ')


while True:
    if nextOpeation == 'y':
        operator = input('which operation to perform (+, -, *, /): ')
        num3 = float(input('Enter next number: '))

        if operator == '+':
            result = result + num3
            print('Answer: ', result)
            nextOpeation = input('Do you want to perform more opration in this calculation: (y, n): ')
            
        elif operator == '-':
            result = result - num3
            print('Answer: ', result)
            nextOpeation = input('Do you want to perform more opration in this calculation: (y, n): ')
            
        elif operator == '*':
            result = result * num3
            print('Answer: ', result)
            nextOpeation = input('Do you want to perform more opration in this calculation: (y, n): ')
            
        elif operator == '/':
            result = result / num3
            print('Answer: ', result)
            nextOpeation = input('Do you want to perform more opration in this calculation: (y, n): ')
            


    else:
        break

print('Thank you for using this Calculator')

