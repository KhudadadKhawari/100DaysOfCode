import random
import time
from turtle import Screen
from player import  Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating CarManager, Scoreboard and Player Objects
car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

# Getting the User input from Keyboard
screen.listen()
screen.onkey(player.move_player, 'Up') # Moves the player up if the user presses Up arrow key

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create Cars Randomly
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_cars()
    # Moves the cars
    car_manager.move_cars()

    # Level Up >> increase score
    if player.ycor() > FINISH_LINE_Y-5: # if player reaches the top of the screen
        scoreboard.increase_level()
        car_manager.increase_cars_speed()

    #Detecting Collision with Cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
