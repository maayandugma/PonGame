from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.goto(self.pos)

    def move_up(self):
        pos_y = self.ycor()
        pos_x = self.xcor()
        if pos_y < 210:
            self.goto((pos_x, pos_y + 30))

    def move_down(self):
        pos_y = self.ycor()
        pos_x = self.xcor()
        if pos_y > -210:
            self.goto((pos_x, pos_y - 30))
