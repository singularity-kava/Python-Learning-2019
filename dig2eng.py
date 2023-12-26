# in this program we want to rename each digit of a received number into english words
num=input ('please enter a digit : ')
dic={
    "1" : "یک",
    "2" : "دو",
    "3" : "سه"
            }

def convert_function(num) :
    newnum=''
    for item in num :
        item=dic.get(item,item)
        newnum += item

    return newnum


new_number=convert_function(num)
print(new_number)