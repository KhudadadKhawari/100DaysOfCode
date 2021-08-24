from turtle import  Screen
import  time, random
from player import  Player
from aliens import  Alien, ALIENS_SPEED_INCREMENT
from scoreboard import  Scoreboard

scr = Screen()
scr.setup(600,600)
scr.bgcolor('black')
scr.tracer(0)

player = Player()
alien = Alien()
scoreboard = Scoreboard()

from turtle import  Turtle
missile = Turtle()
missiles = []
for _ in range(3):
    missile.color("yellow")
    missile.shape("circle")
    missile.shapesize(stretch_len=1, stretch_wid=1)
    missile.penup()
    missile.speed = 15
    missile.state = "ready"
    missile.hideturtle()
    missile.goto(1000,1000)
    missiles.append(missile)

def fire_missile():
    for current_missile in missiles:
        if current_missile.state == "ready":
            current_missile.goto(0, 0)
            current_missile.showturtle()
            current_missile.setheading(player.heading())
            current_missile.state = "fire"
            break

scr.listen()
scr.onkey(player.turn_left,'Left')
scr.onkey(player.turn_right,'Right')
scr.onkey(fire_missile,'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    random_chance = random.randint(1, 14)
    if random_chance == 1:
        alien.create_alien()

    alien.move_aliens()

    for missile in missiles:
        if missile.state == 'fire':
            missile.forward(missile.speed)
            for current_alien in alien.aliens:
                if current_alien.distance(missile) < 30:
                    if missile.position() != (0,0):
                        missile.goto(2000, 2000)
                        current_alien.goto(1000, 1000)  # Sending to aliens garbage location.
                        missile.state = 'ready'
                        scoreboard.increase_score_and_level()
        if missile.xcor() > 280 or missile.xcor() < -280 or missile.ycor() > 280 or missile.ycor() < -280:
            missile.hideturtle()
            missile.state = 'ready'

    for current_alien in alien.aliens:
        if current_alien.distance(player) < 10:
            current_alien.hideturtle()
            current_alien.goto(1000,1000)
            current_alien.forward(0)
            if scoreboard.shield > 0:
                scoreboard.decrease_shield_level()
            else:
                scoreboard.game_over()
                game_is_on = False
    alien.moving_speed = scoreboard.level * ALIENS_SPEED_INCREMENT


scr.exitonclick()
