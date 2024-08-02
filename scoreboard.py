from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-265, 265)
        self.hideturtle()

    def increase_level(self, level):
        self.clear()
        self.write(arg=f"Level: {level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("consolas", 30, "bold"))