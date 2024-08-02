import time
from turtle import Screen

import car_manager
import player
from player import Player
from random import randint
from car_manager import CarManager
from scoreboard import Scoreboard

level = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
screen.listen()
screen.onkeypress(key="Up", fun=timmy.move_up)
cars = CarManager()
score_board = Scoreboard()
score_board.increase_level(level)

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars.all_cars:
        if timmy.distance(car) < 27:
            score_board.game_over()
            game_is_on = False

    if timmy.ycor() > 280:
        level += 1
        timmy.goto(player.STARTING_POSITION)
        score_board.increase_level(level)
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

    if randint(1, 6) == 1:
        cars.create_car()
    cars.move(car_manager.STARTING_MOVE_DISTANCE)
    screen.update()


screen.exitonclick()