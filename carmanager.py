from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y = (-250, 250)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.count = 0
        self.speed = STARTING_MOVE_DISTANCE
        self.cars()

    def cars(self):
        self.count += 1
        if self.count % 6 == 0:
            new_car = Turtle()
            new_car.penup()
            new_car.color = random.choice(COLORS)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(290, random.choice(Y))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            x = car.xcor() - self.speed
            car.goto(x, car.ycor())

    def speed_up(self):
        self.speed += MOVE_INCREMENT
