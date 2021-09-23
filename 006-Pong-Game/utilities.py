from turtle import  Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import  Scoreboard

# Defining the Paddles Positions
RIGHT_PADDLE_POSITION = (350,0)
LEFT_PADDLE_POSITION = (-350,0)

# Creating the Screen
scr = Screen()
scr.setup(height=600, width=800)
scr.bgcolor('black')
scr.title('Pong Game')
scr.tracer(0)

# Creating the Paddles, Ball and ScoreBoard Objects
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()
