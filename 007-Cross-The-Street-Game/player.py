from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_player(self):
        self.goto(self.xcor(),self.ycor() + MOVE_DISTANCE)  # Moves the player alongside Y Axis
        # If the player passes the top wall, brings it back to the starting position for the next level
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

