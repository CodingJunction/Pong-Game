from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
       
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x,0)
        self.pendown()


    def up(self):
        y=self.ycor()+20
        self.penup()
        self.goto(self.xcor(),y)
        self.pendown()

    def down(self):
        y=self.ycor()-20
        self.penup()
        self.goto(self.xcor(),y)
        self.pendown()
    


