from pygame import mixer
import turtle
import random

# plays music
mixer.init()
mixer.music.load("audio/hbd_song.mp3")
mixer.music.play()

# sets background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-150,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-130,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-80,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-70,0)
turtle.color("purple")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-50,0)
turtle.color("lightgreen")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-10,0)
turtle.color("red")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(10,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("lightgreen")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(50,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "turquoise", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-20,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Happy Birthday message
turtle.penup()
turtle.goto(-150, 50) 
turtle.color("pink")
turtle.pendown()
turtle.write("Happy Birthday Stranger!", move=True, font=('Arial', 20, 'normal', 'bold', 'italic', 'underline'))
turtle.color("black")

#exiting the screen on click
bg.exitonclick()