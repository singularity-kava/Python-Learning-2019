
# Pong game for the first game with python
# using turtle module
import turtle
win=turtle.Screen()
win.bgcolor("black")
win.setup(width=800,  height=600)
win.tracer(0)
win.title("This is PONG game")




#paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.setx(-350)
paddle_a.sety(0)
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.color("red")


#paddle B

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.setx(350)
paddle_b.sety(0)
paddle_b.penup()
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.color("red")
paddle_b.speed(0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.setx(0)
ball.sety(0)
ball.penup()
ball.shapesize(stretch_len=2,stretch_wid=2)
ball.color("yellow")
ball.dx=0.5
ball.dy=0.5

# paddle A moving upward
def pad_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    return

# paddle B moving upward
def pad_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    return

# paddle A moving downward
def pad_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    return

# paddle B moving upward
def pad_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    return
# moving the ball
def ball_move():
    # border checking of ball and screen
    if (ball.xcor()>380) or (ball.xcor()<-380):
        ball.dx *= -1
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.dy *= -1
    # border checking of ball and paddles
    if (ball.xcor()>=320) :
        if (ball.ycor()< (paddle_b.ycor()+80) and (ball.ycor()>(paddle_b.ycor()-80))) :
            ball.dx *= -1

    if (ball.xcor()<=-320) :
        if (ball.ycor()< (paddle_a.ycor()+80) and (ball.ycor()>(paddle_a.ycor()-80))) :
            ball.dx *= -1

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    return

# waiting for keyboard to hit W or S for paddle a up and down or Up and Down arrow key for paddle b
win.listen()
win.onkeypress(pad_a_up,"w")
win.onkeypress(pad_a_down,"s")
win.onkeypress(pad_b_up,"Up")
win.onkeypress(pad_b_down,"Down")



# main data
while True:
    win.update()
    ball_move()
# moving the ball in the main menu




