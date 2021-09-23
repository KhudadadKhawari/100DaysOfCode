from turtle import  Turtle

PLAYER_STARTING_SPEED = 5
PLAYER_SPEED_CHANGE = 5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.moving_speed = PLAYER_STARTING_SPEED
        self.create_player()

    def create_player(self):
        self.penup()
        self.color('blue')
        self.shape('arrow')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setposition(0,0)

    def player_heading(self):
        return self.heading()

    def turn_left(self):
        self.left(20)

    def turn_right(self):
        self.right(20)

