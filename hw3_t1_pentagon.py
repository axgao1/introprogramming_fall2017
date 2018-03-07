#!/usr/bin/env python

import turtle

turtle = turtle.Turtle()

startlength = int(10)
decrement = int(2)

while startlength > decrement:
    turtle.forward(startlength)
    turtle.right(108)
    startlength = startlength + decrement

turtle.forward(startlength)

#num_sides = 5
#side_length = 10
#angle = 360.0 / num_sides

#angle = 108
#distance = 20

#for s in range(100):
#    turtle.forward(distance)
#    turtle.right(angle)
#    angle = angle + 5

#def spiral(size):
#    for i in range(50):
#        circle(size)
#        right(20)
#        size = size + 3

#spiral(10)

#input = raw_input()

#startlength = 10
#decrement = 2
#increment = 5
#angle = 108

#while startlength > decrement:
#    turtle.forward(startlength)
#    startlength = startlength + decrement
#    turtle.right(angle)
#    for i in range(100):
#        angle += 2


#turtle.forward(startlength)

# Comment out for debugging.
#turtle.tracer(1000, 1)
#t.ht()

# What you need is a loop that makes
# a slightly open pentagon (sum of angles > 360)
# with sides whose lengths grow slowly with each iteration.

#for t in turtle:
#    turtle.forward(15)
#    turtle.right(25)

#turtle.update()
input("HOLD") # This just allows use to see it.
#turtle.getcanvas().postscript(file="pentagon_tunnel.ps")
