from turtle import Turtle,Screen
import time
from score import Score
from paddle import Paddle
from ball import Ball

pr=0
pl=0


s=Screen()
s.title("Pong Game")
s.setup(800,600)
s.bgcolor("black")

sc=Score()

s.tracer(0)

b=Ball()

    
p1=Paddle(350)
p2=Paddle(-350)

s.listen()
s.onkey(p1.up,"Up")
s.onkey(p1.down,"Down")

s.onkey(p2.up,"w") #to move up
s.onkey(p2.down,"s") #to move down

while True:
    time.sleep(b.sp)
    s.update()
    b.move()

    #walls
    if b.ycor()>280 or b.ycor()<-280:
        b.bounce()


    if b.xcor()>380 :
        b.reset()
        sc.pl+=1
        sc.update()

    if b.xcor()<-380:
        b.reset()
        sc.pr+=1
        sc.update()
        
 

    #paddle
    if b.distance(p1)<40 and b.xcor()>330  :
        b.bouncex()

    if b.distance(p2)<40 and b.xcor()<-330   :
        b.bouncex()
        
 

    

    

s.exitonclick()