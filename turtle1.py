import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=6
sidelength=70
angle=360/numsides
for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()