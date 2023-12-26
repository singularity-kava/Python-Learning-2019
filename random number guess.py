import random
number= random.randint (1,99)
guess= input('what is your guess')
guess= int (guess)
while number !=guess :
        if guess>number :
            print('your guess is higher')
        if guess<number :   
            print ('your guess is smaller')
        else:
            print ('you found the number')
        guess=input('take another guess')
        guess=int(guess)
print('end of the program')

