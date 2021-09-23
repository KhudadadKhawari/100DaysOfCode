from turtle import Turtle


missile = Turtle()
missiles = []
for _ in range(3):
    missile.color("yellow")
    missile.shape("circle")
    missile.shapesize(stretch_len=1, stretch_wid=1)
    missile.penup()
    missile.speed = 15
    missile.state = "ready"
    missile.hideturtle()
    missile.goto(1000,1000)
    missiles.append(missile)

def fire_missile(heading):
    for current_missile in missiles:
        if current_missile.state == "ready":
            current_missile.goto(0, 0)
            current_missile.showturtle()
            current_missile.setheading(heading)
            current_missile.state = "fire"
            break
