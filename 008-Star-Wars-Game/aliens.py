from turtle import  Turtle
from generate_random_position import  generate_random_position

ALIENS_START_MOVING_SPEED = 5
ALIENS_SPEED_INCREMENT = 5

class Alien:
    def __init__(self):
        self.aliens = []
        self.moving_speed = ALIENS_START_MOVING_SPEED
        self.aliens_count = 20
        self.create_alien()

    def create_alien(self):
        new_alien = Turtle('turtle')
        new_alien.color('red')
        new_alien.penup()
        random_position = generate_random_position()
        new_alien.goto(random_position[0],random_position[1])
        heading = new_alien.towards(0,0)
        new_alien.setheading(heading)
        self.aliens.append(new_alien)

    def move_alien(self):
        for alien in self.aliens:
        #     if alien.xcor() > 280 or alien.xcor() < -280 or alien.ycor() > 280 or alien.ycor() < -280:
        #         alien.right(random.randint(45,270))
            alien.forward(self.moving_speed)