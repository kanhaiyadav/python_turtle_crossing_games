from turtle import Turtle
from random import choice, randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(choice(COLORS))
        car.penup()
        car.goto(350, -250 + 25 * randint(1, 19))
        car.setheading(180)
        self.all_cars.append(car)

    def move(self, distance):
        for car in self.all_cars:
            car.forward(distance)
            if car.xcor() < -340:
                self.all_cars.remove(car)
                car.reset()
                car.hideturtle()
