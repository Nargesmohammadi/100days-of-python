from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(270, 250)
        self.update_board()

    def update_board(self):
        self.clear()
        print(self.level)
        self.write(f"level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)