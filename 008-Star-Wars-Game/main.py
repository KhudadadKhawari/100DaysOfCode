from turtle import  Screen
import  time, random
from player import  Player
from aliens import  Alien

scr = Screen()
scr.setup(600,600)
scr.bgcolor('black')
scr.tracer(0)

player = Player()
alien = Alien()


scr.listen()
scr.onkey(player.turn_left,'Left')
scr.onkey(player.turn_right,'Right')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    random_chance = random.randint(1, 10)
    if random_chance == 1:
        alien.create_alien()
    alien.move_alien()




scr.exitonclick()
