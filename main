from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 500)
screen.title("Ping-Pong")
screen.listen()

paddle_l = Paddle((-360,0))
screen.onkey(paddle_l.move_up,"r")
screen.onkey(paddle_l.move_down,"c")

paddle_r = Paddle((360,0))
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")

ball = Ball()
ball.setheading(45)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.wall_touch()

    #Detect collision with paddle
    if ball.xcor() > 340 and ball.distance(paddle_r) < 30 or ball.xcor() < -340 and ball.distance(paddle_l):
        print(ball.distance(paddle_r),ball.distance(paddle_l))

        ball.paddle_touch()

    if ball.xcor() > 400 or ball.xcor() < -400:
        game_is_on = False




screen.exitonclick()
