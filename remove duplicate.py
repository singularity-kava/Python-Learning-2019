number=input ('please enter numbers :')

def remove_dupp(number) :
    newnum=[]
    for item in range(len(number)) :
        if number[item] not in newnum:
            newnum.append(number[item])
    return newnum


num = remove_dupp(number)
print (num)