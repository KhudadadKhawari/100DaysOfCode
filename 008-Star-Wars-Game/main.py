from turtle import  Screen
import  time, random
from player import  Player
from aliens import  Alien
# from missile import  Missile

scr = Screen()
scr.setup(600,600)
scr.bgcolor('black')
scr.tracer(0)

player = Player()
alien = Alien()
# missile = Missile()

# def shoot_the_target():
#     player_heading = player.player_heading()
#     missile.fire_missile(player_heading)

from turtle import  Turtle
missile = Turtle()
missiles = []
for _ in range(3):
    missile.color("yellow")
    missile.shape("circle")
    missile.shapesize(0.5)
    missile.penup()
    missile.speed = 15
    missile.state = "ready"
    missile.hideturtle()
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
                if missile.distance(current_alien) < 20:
                    missile.hideturtle()
                    missile.state = 'ready'
                    current_alien.hideturtle()
        if missile.xcor() > 280 or missile.xcor() < -280 or missile.ycor() > 280 or missile.ycor() < -280:
            missile.hideturtle()
            missile.state = 'ready'





scr.exitonclick()
