from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("../Day29/data.txt") as date:
            self.high_score = int(date.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # self.write(arg="score", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../Day29/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    # self.goto(0, 0)
    # self.write("Game over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.write(arg="score", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()
