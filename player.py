from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, position = STARTING_POSITION):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.limit = FINISH_LINE_Y

    def move_up(self):
        self.forward(MOVE_DISTANCE)
