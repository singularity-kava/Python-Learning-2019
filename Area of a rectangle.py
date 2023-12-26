# this program computes the area of a rectangle and makes sure that you entered correct numbers
# if you used unformatted numbers or used negative or zero numbers it will tell you to correct that using exceptions 
try:
    value= False
    while not value:
            l=int(input(" please enter length of a rectangle in order to compute its area : "))
            w=int(input(" please enter width of a rectangle in order to compute its area : "))
            if l<=0 or w<=0 :
                 print('please enter positive and non-zero numbers')
            else:
                value=True
    area = l * w
    print(f'area of this rectangle is : {area}')

except ValueError:
        print('invalid input')