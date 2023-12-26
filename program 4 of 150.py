# in this program we want to read the height and base of a triangle and compute its area in a function

def area(h,b):
    return h*b

value=False
print('please enter height and base of a triangle :' )
while not value:
    height=int(input('height : '))
    base=int(input('base : '))
    if (height<=0) or (base<=0) :
        print('please enter valid numbers ')
    else:
        break
print(area(height,base))

