from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.speed_value = STARTING_MOVE_DISTANCE
        self.color(choice(COLORS))
        self.goto(320, randint(-250, 250))

    def move(self):
        self.forward(self.speed_value * -1)

    @staticmethod
    def speed_increase():
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
