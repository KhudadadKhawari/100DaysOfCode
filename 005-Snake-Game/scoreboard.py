from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265) # positioning the score board at the top - middle
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    # Displaying the Game Over text, get a parameter even the snake collided with it's tail or the walls
    def game_over(self, param):
        self.goto(0, 0)
        self.write(f"GAME OVER! \n{param}", align=ALIGNMENT, font=FONT)

    #updating the scoreboard text frequently
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # increase the score by 1
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Arial", 24, 'normal'))