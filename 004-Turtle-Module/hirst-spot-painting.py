# to run this you need to install colorgram by:
# pip install colorgram
import colorgram
import turtle as t
import random

t.colormode(255) #Enable RGB color mode in turtle
pen = t.Turtle()
pen.speed('fastest')
pen.pensize(15)
pen.penup() # to avoid drawing the lines between dots
pen.hideturtle() #hiding the turtle pointer so it will look cool
#importing the image and extracting 100 colors from the image by colorgram package
color_from_image = colorgram.extract('image.jpg', 100)

#Extracting the RGB Colors from the image
def color_extraction(colors):
    extracted_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors_tuple = (r, g, b)
        extracted_colors.append(colors_tuple)
    return extracted_colors

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    pen.dot(20,random.choice(color_extraction(color_from_image)))
    pen.forward(50)
    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


scr = t.Screen()
scr.exitonclick()