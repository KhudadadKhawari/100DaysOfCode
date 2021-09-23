from turtle import  Turtle


STARTING_POSITION = [(0,0),(-20,0),(-40,0)] # Snake Starting position for the 3 segments.
MOVE_DISTANCE = 10 # Change this to increase / decrease the snake moving speed
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] # The segments will increase if the snake hit the food
        self.create_snake()
        self.head = self.segments[0] # to avoid repeating segment[0] creating the head.

    def create_snake(self):
        for position in STARTING_POSITION: # Joining the first 3 segments together there won't be any gap between them.
            self.add_segment(position) # Performing the add_segment method

    # Gets the position for the segment and add it to the snake
    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    # Adds a new segment after the last segment
    def extend(self):
        self.add_segment(self.segments[-1].position())
    # Moves the segments after each other. so the 3rd segment will follow the 2nd one and the 2nd one will follow the 1st segment
    # So you will need to move the first segment only. the other segments will follow it.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Moves the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Moves the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Moves the snake to the left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Moves the snake to the right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)