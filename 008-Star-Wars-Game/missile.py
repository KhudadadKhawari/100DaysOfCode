from turtle import  Turtle

class Missile:
    def __init__(self):
        super().__init__()
        self.missiles = []
        self.create_missile()

    def create_missile(self):
        new_missile = Turtle('circle')
        new_missile.shapesize(20)
        new_missile.color('yellow')
        new_missile.speed = 5
        new_missile.state = 'ready'
        new_missile.hideturtle()
        self.missiles.append(new_missile)

    def fire_missile(self,heading):
        for missile in self.missiles:
            if missile.state == 'ready':
                missile.goto(0, 0)
                missile.showturtle()
                missile.setheading(heading)
                missile.state = 'fire'
                break
    def return_missiles(self):
        return_missiles = []
        for missile in self.missiles:
            return_missiles.append(missile)
        return return_missiles


