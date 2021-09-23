from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Scoreboard for the Left Player
        self.goto(-100,260)
        self.write(self.left_score, align='center',font=('Times New Roman', 20, "normal"))
        # Scoreboard for the Right Player
        self.goto(100,260)
        self.write(self.right_score, align='center',font=('Times New Roman', 20, "normal"))

    # Increases the Left Player's Score by 1
    def increase_left_paddle_score(self):
        self.left_score += 1
        self.update_scoreboard()
    # Increases the Right Player's Score by 1
    def increase_right_paddle_score(self):
        self.right_score += 1
        self.update_scoreboard()