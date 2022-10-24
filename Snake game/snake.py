from turtle import Turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # THE FIRST SEGMENTS, WE CAN NOT WRITE THIS ABOVE THE CREATE SNAKE.
        self.head = self.segments[0]

    def create_snake(self):
        for positions in SNAKE_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(positions)
        self.segments.append(snake)

    def reset(self):
        # for clear the former snake in the screen when we lose.
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to snake.
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # self.segments[0].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

    # add methods for control the snake with keypress

    def snake_up(self):
        # self.segments[0].setheading(90)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)