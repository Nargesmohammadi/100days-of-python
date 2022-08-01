from turtle import Turtle, Screen
from player import Player
from carmanager import CarManager
from scoreboardd import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Crossing game")
screen.tracer(0)

player = Player()
car = CarManager()


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.cars()
    car.move()












screen.exitonclick()
