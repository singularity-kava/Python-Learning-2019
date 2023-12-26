# this class has a method called bark and an object called 'name'
# i use a construct to specify values for this class

class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f" {self.name} talks too much, please be quiet ")

newname=input('> ')

dog1=Dog(newname)
print(dog1.name)
dog1.bark()
