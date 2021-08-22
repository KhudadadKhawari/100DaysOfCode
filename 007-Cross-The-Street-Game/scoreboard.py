from turtle import  Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-280, 250) # Moves the Scoreboard to the top left
        self.write(f"Level: {self.level}", align='left', font=FONT)

    # increases the level by 1
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(0,0)
        self.write("Game Over!", align='center', font=FONT)