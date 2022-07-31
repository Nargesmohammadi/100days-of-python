from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# create the screen
screen = Screen()

screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create right and left paddle.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
# create ball
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "W")
screen.onkey(left_paddle.down, "S")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # detecting collision with wall
    if ball.ycor() > 220 or ball.ycor() < -220:
        # need the bounce
        ball.bounce()
screen.exitonclick()
