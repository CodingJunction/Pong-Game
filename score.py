from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pl=0
        self.pr=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.pl,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.pr,align="center",font=("Courier",80,"normal"))


        
