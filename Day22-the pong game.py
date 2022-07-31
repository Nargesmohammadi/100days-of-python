from turtle import Turtle,Screen


screen = Screen()

screen.bgcolor("green")
screen.setup(height=700, width=900)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(400, 0)


def up():
    y = paddle.ycor() + 30
    paddle.goto(paddle.xcor(), y)


def down():
    y = paddle.ycor() - 30
    paddle.goto(paddle.xcor(), y)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")


game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()