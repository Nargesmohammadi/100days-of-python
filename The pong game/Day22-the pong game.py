from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create the screen
screen = Screen()

screen.bgcolor("green")
screen.setup(width=850, height=600)
screen.title("Pong")
screen.tracer(0)


# create right and left paddle.
right_paddle = Paddle((400, 0))
left_paddle = Paddle((-400, 0))
# create ball
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "W")
screen.onkey(left_paddle.down, "S")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detecting collision with wall
    if ball.ycor() > 220 or ball.ycor() < -220:
        # need the bounce
        ball.bounce_y()

    # detect collision with right_paddle and left_paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when ball misses by right paddle.
    if ball.xcor() > 420:
        ball.reset_position()
        # increase the score
        scoreboard.left_point()

    # detect when ball misses by left paddle.
    if ball.xcor() < -420:
        ball.reset_position()
        # increase the score
        scoreboard.right_point()
screen.exitonclick()
