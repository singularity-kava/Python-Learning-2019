import turtle
import winsound

win=turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor("black")
win.tracer(0)
win.title("this is a PONG game!")
scorea=0
scoreb=0
# paddle A
pa=turtle.Turtle()
pa.shape("square")
pa.shapesize(stretch_len=1, stretch_wid=5)
pa.color("white")
pa.speed(0)
pa.penup()
pa.goto(-350,0)


# paddle B
pb=turtle.Turtle()
pb.shape("square")
pb.shapesize(stretch_len=1, stretch_wid=5)
pb.color("white")
pb.speed(0)
pb.penup()
pb.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.dx=0.25
ball.dy=0.25
ball.penup()
ball.goto(0,0)

# pen : Comments and Scores
pen=turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.goto(0,-280)
pen.write(f'Use Arrow keys or W for UP and S for Down',align="center",font=("courier",10,"italic"))
pen.goto(0,260)
pen.write( f'SCORE A = {scorea}  , SCORE B = {scoreb}', align="center", font="arial")




# paddle A upward movement
def pada_up():
    y=pa.ycor()
    if y<240:
        y+=20
    pa.sety(y)
    return


# paddle B upward movement
def padb_up():
    y=pb.ycor()
    if y<240:
        y+=20
    pb.sety(y)
    return

# paddle A downward movement
def pada_down():
    y=pa.ycor()
    if y>-240:
        y-=20
    pa.sety(y)
    return

# paddle B downward movement
def padb_down():
    y=pb.ycor()
    if y > -240:
        y-=20
    pb.sety(y)
    return


#onpress keyboard listening for W and S or Arrows key

win.listen()
win.onkeypress(pada_up,"w")
win.onkeypress(pada_down,"s")
win.onkeypress(padb_up,"Up")
win.onkeypress(padb_down,"Down")

# main
#--------------------------------------------------------

while True :
      win.update()
      ball.sety(ball.ycor()+ball.dy)
      ball.setx(ball.xcor()+ball.dx)
# border checking
      if (ball.ycor()>290) or (ball.ycor()<-290):
           ball.dy *= -1

# Hitting left and right plane and SCORE
      if ball.xcor()>400:
          scorea +=1
          ball.goto(0,0)
          ball.dx *=-1
          pen.clear()
          pen.goto(0, -280)
          pen.write(f'Use Arrow keys or W for UP and S for Down', align="center", font=("courier", 10, "italic"))
          pen.goto(0,260)
          pen.write(f'SCORE A = {scorea}  , SCORE B = {scoreb}', align="center", font="arial")


      if ball.xcor() <-400:
            scoreb += 1
            ball.goto(0, 0)
            ball.dx *= -1
            pen.clear()
            pen.goto(-0, -280)
            pen.write(f'Use Arrow keys or W for UP and S for Down', align="center", font=("courier", 10, "italic"))
            pen.goto(0, 260)
            pen.write(f'SCORE A = {scorea}  , SCORE B = {scoreb}', align="center", font="arial")


# Ball collision with paddles
      if (ball.xcor()>330 and ball.xcor()<350) and ((ball.ycor()<pb.ycor()+60)  and  (ball.ycor()>pb.ycor()-60)) :
         ball.goto(330,ball.ycor())
         ball.dx *=-1
         winsound.PlaySound("Ball_Bounce.wav",winsound.SND_ASYNC)

      if (ball.xcor()<-330 and ball.xcor()>-350) and ((ball.ycor()<pa.ycor()+60) and  (ball.ycor()>pa.ycor()-60)) :
         ball.goto(-330,ball.ycor())
         ball.dx *=-1
         winsound.PlaySound("Ball_Bounce.wav", winsound.SND_ASYNC)







    