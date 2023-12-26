import math
try:
    age=int(input('please enter a number'))
    print(f'your age is {age}')

except ValueError:
    print('this value is not valid')
except ZeroDivisionError:
    print()
