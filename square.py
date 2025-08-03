import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
pen=turtle.Turtle()
pen.penup()
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.right(180)
pen.pendown()
numside=4
for i in range(numside):
    pen.forward(200)
    pen.right(90)
turtle.done()