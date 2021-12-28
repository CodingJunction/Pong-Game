from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.x_val=10
        self.y_val=10
        self.sp=0.1

    def move(self):
        self.penup()
        self.goto(self.xcor()+self.x_val,self.ycor()+self.y_val)
        self.pendown()

    def bounce(self):
      
        self.y_val*=-1
        self.penup()
        self.goto(self.xcor()+self.x_val+10,self.ycor()+self.y_val+10)
        self.sp*=0.09
    

    def bouncex(self):
   
        self.x_val*=-1
        self.penup()
        self.goto(self.xcor()+self.x_val,self.ycor()+self.y_val)
        self.sp*=0.09
      

    def reset(self):
      self.penup()
      self.goto(0,0)
      self.pendown()
      self.bouncex()
      self.sp=0.1