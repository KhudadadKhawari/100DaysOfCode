from turtle import  Turtle
from generate_random_position import  generate_random_position

ALIENS_START_MOVING_SPEED = 3
ALIENS_SPEED_INCREMENT = 3

class Alien:
    def __init__(self):
        self.aliens = [] #creating a list of alliens
        self.moving_speed = ALIENS_START_MOVING_SPEED
        self.create_alien()

    def create_alien(self):
        new_alien = Turtle('turtle')
        new_alien.color('red')
        new_alien.penup()
        new_alien.speed(self.moving_speed)
        random_position = generate_random_position() #generating a random position to send alien to that post
        new_alien.goto(random_position[0],random_position[1])
        heading = new_alien.towards(0,0) #Every alien should go towards center where the player is
        new_alien.setheading(heading)
        self.aliens.append(new_alien) #appending to the aliens list

    # Moving all the aliens
    def move_aliens(self):
        for alien in self.aliens:
            # if the alien get outside the window
            if alien.xcor() > 280 or alien.xcor() < -280 or alien.ycor() > 280 or alien.ycor() < -280 :
                alien.setheading(alien.towards(0,0)) # turns back the alien towards the center
            if alien.position() != (1000.0,1000.0): # this is the garbage position for aliens which are hit by the player
                alien.forward(self.moving_speed) # stops the aliens from moving in the aliens garbage position
