import turtle
import winsound

# creating screen window
windows=turtle.Screen()
windows.clear()
windows.bgcolor("green")
windows.setup(width=800, height= 600)
windows.tracer(0)
windows.title(" this program is reprogramming to remember the previous sets")


# creating a circle A
a=turtle.Turtle()
a.shape("circle")
a.shapesize(stretch_len= 2, stretch_wid= 2)
a.color('red')
a.penup()
a.goto ( -300,0)
a.dx=0.25
a.dy=-0

# creating a cirgle B
b=turtle.Turtle()
b.shape("square")
b.shapesize(stretch_len= 2, stretch_wid= 2)
b.color('yellow')
b.penup()
b.goto ( 300,0)
b.dx=-0.25
b.dy=0

# function to move the objects A and B
def moving_ball(name) :
    y=name.ycor()
    x=name.xcor()
    if collision(a,b):
        a.dx *= -1
        a.dy *= -1
        b.dx *= -1
        b.dy *= -1

    a.setx(a.xcor() + a.dx)
    a.sety(a.ycor() + a.dy)
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)


# collision of the balls A and B
def collision(a,b) :
   if (a.ycor()==b.ycor()) and  (a.xcor()==b.xcor())  :
        return True
while True :
    windows.update()
    moving_ball(a)
    moving_ball(b)




