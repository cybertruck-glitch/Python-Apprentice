"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina                # Create a turtle named tina
tina.circle(50)
tina.penup()
tina.goto(0,100)
tina.pendown()
tina.circle(60)
turtle.exitonclick() 



