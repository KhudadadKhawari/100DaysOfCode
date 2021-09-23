from  turtle import Turtle, Screen

DEGREE = 360
shape = 3
angle = 0
pen = Turtle()
colors = ['black','blue','green','yellow','orange','red','purple','grey','pink','blue']
for color in colors:
    angle = DEGREE / shape
    pen.pencolor(color)
    for _ in range(shape):
        pen.forward(100)
        pen.right(angle)
    shape += 1


scr = Screen()
scr.exitonclick()