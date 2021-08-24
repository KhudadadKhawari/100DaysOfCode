from turtle import  Turtle

SHIELD_LEVEL = 5
SCORE_PER_LEVEL = 5
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.shield = SHIELD_LEVEL
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-280, 250) # Moves the Scoreboard to the top left
        self.write(f"Level: {self.level} Score: {self.score} Shield: {self.shield}", align='left', font=FONT)

    # increases the score and level
    def increase_score_and_level(self,):
        self.score += 1
        if self.score > SCORE_PER_LEVEL:
            self.level += 1
            self.shield += 1
            self.score = 0
        self.update_scoreboard()

    def decrease_shield_level(self):
        self.shield -= 1
        self.update_scoreboard()



    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,0)
        total_hits = self.level * 5 + self.score


        with open('top_score.txt', 'r') as old_file:
            data = old_file.read()
            if data:
                best_total_hits = int(data)
            else:
                best_total_hits = 0
        self.write(f"Game Over! \nTotal Hits: {total_hits}\nBest Total Hits: {best_total_hits}", align='center', font=FONT)
        with open('top_score.txt', 'w') as file:
            if best_total_hits < total_hits:
                file.write(str(total_hits))
            else:
                file.write(str(best_total_hits))