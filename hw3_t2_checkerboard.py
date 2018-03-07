#!/usr/bin/env python 

import turtle

t = turtle.Turtle()

# Comment out for debugging.
turtle.tracer(1000, 1)
t.ht()

# Here, you need to create 64 squares -- 
#  eight columns and eight rows.
# For (ahem!) each, you make the same square.
# but sometimes the square is colored, 
# and sometimes it is not.  What is the condition?

turtle.update()
input("HOLD")

t.getscreen().getcanvas().postscript(file="checkerboard.ps")
