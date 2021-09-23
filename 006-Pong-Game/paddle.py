from turtle import  Turtle


class Paddle(Turtle):

    def __init__(self,post):
        super().__init__()
        self.create_paddle(post)

    def create_paddle(self,post):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.penup()
        self.goto(post)

    # Moves the Paddle up alongside Y Axis
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    # Moves the Paddle down alongside Y Axis
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)