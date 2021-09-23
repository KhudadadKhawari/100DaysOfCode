from turtle import  Turtle

SHIELD_STRENGTH = 5
SCORE_PER_LEVEL = 5
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.shield_strength = SHIELD_STRENGTH # Default shield Strength
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-280, 250) # Moves the Scoreboard to the top left
        self.write(f"Level: {self.level} Score: {self.score} Shield Strength: {self.shield_strength}", align='left', font=FONT)

    # increases the score and level
    def increase_score_and_level(self,):
        self.score += 1
        if self.score > SCORE_PER_LEVEL: # after each 5 hits the level will increase
            self.level += 1
            self.shield_strength += 1
            self.score = 0
        self.update_scoreboard()

    def decrease_shield_strength(self):
        self.shield_strength -= 1
        self.update_scoreboard()


    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,0)
        total_hits = self.level * 5 + self.score

        # Getting the Best score from the saved file on the disk
        past_total_hits = 0
        try:
            with open('best_score.txt', 'r') as old_file:
                data = old_file.read()
                if data:
                    past_total_hits = int(data)
        except FileNotFoundError:
            pass

        with open('best_score.txt', 'w') as file:
            if past_total_hits < total_hits:
                file.write(str(total_hits))
            else:
                file.write(str(past_total_hits))

        if past_total_hits > total_hits:
            best_total_hits = past_total_hits
        else:
            best_total_hits = total_hits

        self.write(f"Game Over! \nTotal Hits: {total_hits}\nBest Total Hits: {best_total_hits}", align='center', font=FONT)

