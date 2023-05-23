import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
from turtle import Turtle
from random import randint


def net(x, y):
    my_net = Turtle()
    my_net.penup()
    my_net.goto(x=x, y=y)
    for n in range(100):
        my_net.pendown()
        my_net.forward(20)
        my_net.penup()
        my_net.forward(20)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
manager = CarManager()
level = ScoreBoard()
i = -250
for n in range(6):
    net(-300, i)
    i += 100

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.generate_cars()
    manager.cars_moves()
    for car in manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
    if player.ycor() == 280:
        player.start()
        manager.increase_speed()
        level.add_level()
screen.exitonclick()
