from turtle import  Screen
import turtle as t
from snake import  Snake
from food import  Food
from scoreboard import Scoreboard

import  time
scr = Screen()
scr.setup(width=600,height=600) #changing the screen size to 600x600 pixels
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0) #tracer() This function is used to turn turtle animation on or off and set a delay for update drawings.

# Creating the snake, food and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Getting the key pressed by the user and performing a specific function
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")



game_is_on = True # it will change to false only if the snake head collides with it's tail or the walls.
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    #Detecting collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detecting Collision with Walls:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over('Collided with Wall')

    #Detecting Collision with Tail:
    # if head collides with any segment in the tail:
        #trigger game_over
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 1:
            print(snake.head.distance(segment))
            game_is_on = False
            scoreboard.game_over('Collided with Tail')

t.done()