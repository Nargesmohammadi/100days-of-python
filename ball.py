from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        # print(x)
        # print(y)
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

