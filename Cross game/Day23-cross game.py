from turtle import Screen
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
car_manager = CarManager()
scoreboardd = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars()
    car_manager.move()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboardd.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.start()
        car_manager.speed_up()
        scoreboardd.increase_level()


screen.exitonclick()
