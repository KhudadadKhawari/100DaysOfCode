from turtle import  Turtle
import random
#creating the food
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() #penup so it won't draw the line
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # changing the size of the food which is a fat dot.LOL
        self.color("green")
        self.speed("fastest")
        self.refresh()
    #Choosing the next random location where the food is going to appear
    def refresh(self):
        random_x = random.randint(-280, 280) # since the screen size is 600x600 so half of that is 300 divided by 2 coordinates x and y 20px is for the walls
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)