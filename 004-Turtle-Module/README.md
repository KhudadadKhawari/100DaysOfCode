# Working With Turtle Module in Python
## Drawing Colorful Polygonal shapes

**Description:** Draw a triangle, square, pentagon, hexagon, heptagon, octagon nonage and decagon using turtle module in python  <br>
**Solution:** total degree is going to be 360. so it is divided by 3 to find the angles of triangle, by 4 to find the angles of square and so on.... <br>
shape = 3...10 <br>
angle = 360 /shape <br>
colors = list of different colors <br>

**Process:** The turtle will move forward to draw a straight line then will turn right by the angle(360/shape). this loop will continue to the value of shape.<br>

![Polygonal Shapes](https://github.com/KhudadadKhawari/100DaysOfCode/blob/main/004-Turtle-Module/colorfull-polygonal-shapes.jpg?raw=true)

## Extracting colors from Image
## Hirst spot painting
**Description:** Draw a hirst spot painting by turtle module in python. import colors from an external image and use the colors to draw the painting. <br>
**Solution:** To Extract the colors from an external Image I'm going to use [colorgram](https://pypi.org/project/colorgram.py/) package.


![hirst-spot-painting](https://github.com/KhudadadKhawari/100DaysOfCode/blob/main/004-Turtle-Module/hirst-spot-painting.jpg?raw=true)

## Random Walk
**Description:** Draw a colorful random walk path using turtle in python. <br>
**Solution:** to do this the turtle.setheading function must generate some random angles. in this case I'm using random module to choose from a set of angles. 

![random-walk](https://github.com/KhudadadKhawari/100DaysOfCode/blob/main/004-Turtle-Module/random-walk.jpg?raw=true)