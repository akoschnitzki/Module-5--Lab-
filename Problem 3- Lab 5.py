#Name- Alexander Koschnitzki
#Date - 10-28-21
#CSS- 225

import turtle
s = turtle.Screen()
t = turtle.Turtle()
sides = int(input("Enter the number of sides:"))
length = int(input("Enter the length of the side"))
col = input("Enter the color of your polygon:")
t.fillcolor(col)
t.begin_fill()
for x in range(sides):
    t.forward(length)
    t.right(360/sides)
t.end_fill()
s.mainloop()

# What this program does is that it can be able to create a polygon with
# any number and any color. Once you input the information, it is able to
# draw the shape for you with the color that you picked. It is able to work
# with any number and color that you input.