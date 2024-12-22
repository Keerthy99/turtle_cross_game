import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
score=Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

#Detection with car
    for car in car_manager.all_cars:
       if  car.distance(player)<20:
           game_is_on=False
           score.game_over()

#Detect the other end
    if player.is_at_finsh_line():
        player.go_to_start()
        car_manager.increase_speed()
        score.increase_level()

#Updating the level





screen.exitonclick()