try:
    l=int(input(" please enter length of a rectangle in order to compute its area : "))
    w=int(input(" please enter width of a rectangle in order to compute its area : "))
    if l<=0 or w<=0 :
    print('please enter positive and non-zero numbers')
    area = l * w
    print(f'area of this rectangle is : {area}')

except ValueError:
        print('invalid input')
