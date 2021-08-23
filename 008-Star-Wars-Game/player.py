from turtle import  Turtle

PLAYER_STARTING_SPEED = 5
PLAYER_SPEED_CHANGE = 5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.moving_speed = PLAYER_STARTING_SPEED
        self.missiles = []
        self.missiles_count = 50
        self.create_player()
        self.create_missile()

    def create_player(self):
        self.penup()
        self.color('blue')
        self.shape('arrow')
        self.shapesize(stretch_wid=1, stretch_len=3)

    def create_missile(self):
        for _ in range(self.missiles_count):
            new_missile = Turtle('circle')
            new_missile.penup()
            new_missile.hideturtle()
            new_missile.color('yellow')
            self.missiles.append(new_missile)

    def select_missile(self,missile_number):
        self.missiles[missile_number].goto()

    def shoot_target(self):
        pass

    def turn_left(self):
        self.left(20)

    def turn_right(self):
        self.right(20)

