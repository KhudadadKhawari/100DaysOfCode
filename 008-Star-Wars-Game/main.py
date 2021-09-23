from turtle import  Screen
import  time, random
from player import  Player
from aliens import  Alien, ALIENS_SPEED_INCREMENT
from scoreboard import  Scoreboard
from missiles import *

# Setting up the Screen
scr = Screen()
scr.setup(600,600)
scr.bgcolor('black')
scr.tracer(0)

# Creating the Objects
player = Player()
alien = Alien()
scoreboard = Scoreboard()

# Getting the user input from the keyboard

def fire_current_missile():
    fire_missile(player.heading())



scr.listen()
scr.onkey(player.turn_left,'Left')
scr.onkey(player.turn_right,'Right')
scr.onkey(fire_current_missile,'space')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()

    # Decreasing the speed of creating new alien objects
    random_chance = random.randint(1, 14)
    if random_chance == 1:
        alien.create_alien()

    alien.move_aliens() # aliens start moving

    for missile in missiles:
        if missile.state == 'fire':
            missile.forward(missile.speed) # shooting the missile
            for current_alien in alien.aliens:
                if current_alien.distance(missile) < 30: # if the missile touches the aline object
                    if missile.position() != (0,0): # sending the missile to the "MISSILES WAIT LOCATION" if it's not in the center
                        missile.goto(2000, 2000) # MISSILES WAIT LOCATION
                        current_alien.goto(1000, 1000)  # Sending alien to aliens garbage location.
                        missile.state = 'ready'
                        scoreboard.increase_score_and_level()
        if missile.xcor() > 280 or missile.xcor() < -280 or missile.ycor() > 280 or missile.ycor() < -280: # if missile didn't touch any alien object after shooting, it will get out of play area.
            missile.hideturtle() # hiding missile
            missile.goto(2000,2000) # sending missile to WAIT LOCATION
            missile.state = 'ready'


    for current_alien in alien.aliens:
        if current_alien.distance(player) < 10: # if the alien hits the player
            current_alien.hideturtle()
            current_alien.goto(1000,1000) # sending the alien to the alien garbage location
            current_alien.forward(0) # stopping the alien form moving
            if scoreboard.shield_strength > 0: # if user has shield level
                scoreboard.decrease_shield_strength()
            else:
                scoreboard.game_over()
                game_is_on = False
    alien.moving_speed = scoreboard.level * ALIENS_SPEED_INCREMENT # increases the aliens moving speed according to the current level


scr.exitonclick()
