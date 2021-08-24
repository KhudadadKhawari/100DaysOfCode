from turtle import  Turtle
from generate_random_position import  generate_random_position

ALIENS_START_MOVING_SPEED = 3
ALIENS_SPEED_INCREMENT = 3

class Alien:
    def __init__(self):
        self.aliens = []
        self.moving_speed = ALIENS_START_MOVING_SPEED
        self.create_alien()

    def create_alien(self):
        new_alien = Turtle('turtle')
        new_alien.color('red')
        new_alien.penup()
        new_alien.speed(self.moving_speed)
        random_position = generate_random_position()
        new_alien.goto(random_position[0],random_position[1])
        heading = new_alien.towards(0,0)
        new_alien.setheading(heading)
        self.aliens.append(new_alien)

    def move_aliens(self):
        for alien in self.aliens:
            print(alien.position())
            if alien.xcor() > 280 or alien.xcor() < -280 or alien.ycor() > 280 or alien.ycor() < -280 :
                alien.setheading(alien.towards(0,0))
            if alien.position() != (1000.0,1000.0):
                alien.forward(alien.speed())

