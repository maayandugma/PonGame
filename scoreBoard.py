# from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 210)
        self.l_score = 0
        self.r_score = 0
        self.write(arg=f"{self.l_score}:{self.r_score}",font=('Ariel',20,'normal'))
        self.pendown()
    def update_score(self):
        self.write(arg=f"{self.l_score}:{self.r_score}",font=('Ariel',20,'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def the_winner(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write(arg=f"the winner is Left Paddle", font=('Ariel', 40, 'normal'), align='center')
        else:
            self.write(arg=f"the winner is Right Paddle", font=('Ariel', 40, 'normal'), align='center')
