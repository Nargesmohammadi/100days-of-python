from turtle import Turtle, Screen

from paddle import Paddle

screen = Screen()

screen.bgcolor("green")
screen.setup(width=900, height=700)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "W")
screen.onkey(left_paddle.down, "S")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
