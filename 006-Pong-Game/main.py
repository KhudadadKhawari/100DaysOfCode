from utilities import  scr, right_paddle, left_paddle, ball, scoreboard
import time

# Getting the User Input from Keyboard
scr.listen()

# Player controlling the Right paddle
scr.onkey(right_paddle.go_up, 'Up')
scr.onkey(right_paddle.go_down, 'Down')

# Player Controlling the Left Paddle
scr.onkey(left_paddle.go_up, 'w') # in case the CAPSLOCK is OFF
scr.onkey(left_paddle.go_up, 'W') # in case the CAPSLOCK is ON
scr.onkey(left_paddle.go_down, 'S') # in case the CAPSLOCK is OFF
scr.onkey(left_paddle.go_down, 's') # in case the CAPSLOCK is ON

game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed) # increase / decrease the ball moving speed
    scr.update()
    ball.move()

    #Detecting Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detecting Collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detecting if the Right Paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_paddle_score()

    #Detecting if the Left Paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_paddle_score()

scr.exitonclick()