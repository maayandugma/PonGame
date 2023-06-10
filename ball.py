from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_right_up(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def change_direction_down(self):
        self.setheading(180)
        self.move_right_down()

    def move_right_down(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def move_left_up(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def move_left_down(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def wall_touch(self):
        self.y_move *= -1

    def paddle_touch(self):
        self.x_move *= -1