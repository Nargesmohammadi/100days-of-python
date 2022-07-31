from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()

    def paddle_position(self):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()
        self.paddle.goto(400, 0)

    def up(self):
        y = paddle.ycor() + 30
        paddle.goto(paddle.xcor(), y)

    def down(self):
        y = paddle.ycor() - 30
        paddle.goto(paddle.xcor(), y)



paddle = Paddle()
