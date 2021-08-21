from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)

    # Move's the ball according to the x and y Axis
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    # moves the ball to contra position according to Y Axis
    def bounce_y(self):
        self.y_move *= -1

    # moves the ball to contra position according to X Axis
    def bounce_x(self):
        self.x_move *= -1
        self.moving_speed *= 0.9

    # Reset the Ball position to the Center
    def reset_position(self):
        self.goto(0,0)
        self.moving_speed = 0.1 # Decreases the Ball Moving speed
        self.bounce_x()


