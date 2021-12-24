# Hello Welcome to Turtle animation source code 

# import module 

import turtle 
turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.speed(0.5)
color = ["red", "blue", "green", "orange"]
color1 = ["white", "brown", "green", "yellow"]


for a in range (9):
    for i in color:

        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)

for a in range (9):
    for i in color1:

        turtle.color(i)
        turtle.circle(100)
        turtle.right(10)






# Main loop
turtle.mainloop()
    