from turtle import *

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.add_level()

    def add_level(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"LEVEL: {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT)

