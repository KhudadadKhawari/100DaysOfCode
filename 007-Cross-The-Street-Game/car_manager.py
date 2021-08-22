from turtle import  Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super(CarManager, self).__init__()
        self.moving_speed = 5
        self.cars = [] # List of Cars which will move from right to the left
        self.create_cars()

    def create_cars(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shape('square')
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.goto(280,random.randint(-250,250))  # Send the car created to a random position to the right alongside Y axis
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.moving_speed) # Moves the cars from right to the left

    def increase_cars_speed(self):
        self.moving_speed += MOVE_INCREMENT # increases the cars speed by 2x , 2*5(normal) = 10
        self.move_cars()