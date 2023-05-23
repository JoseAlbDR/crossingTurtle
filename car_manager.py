from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.increment = 0

    def generate_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(choice(COLORS))
            car.penup()
            car.goto(300, randint(-260, 280))
            self.car_list.append(car)

    def cars_moves(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + self.increment)

    def increase_speed(self):
        self.increment += MOVE_INCREMENT
