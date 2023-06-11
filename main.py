from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard
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

score = Scoreboard()
ball = Ball()
ball.setheading(45)

time_wait = 0.1
counter_bounce = 0
def check_counter(counter):
    if counter % 4 == 0:
        return True
    else:
        return False

while True:
    if score.l_score < 2 and score.r_score < 2:
        print(score.l_score)
        # game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(time_wait)
            ball.move()

            # Detect collision with wall
            if ball.ycor() > 230 or ball.ycor() < -230:
                ball.wall_touch()

            #Detect collision with paddle
            if ball.xcor() == 340 and ball.distance(paddle_r) < 30 or ball.xcor() == -340 and ball.distance(paddle_l) < 30:
                ball.paddle_touch()
                counter_bounce += 1
                if check_counter(counter_bounce):
                    time_wait = time_wait / 2


            if ball.xcor() > 400:
                score.l_point()
                ball.reset_position()
                game_is_on = False


            if ball.xcor() < -400:
                score.r_point()
                ball.reset_position()
                game_is_on = False

    else:
        score.the_winner()
        break


screen.exitonclick()
