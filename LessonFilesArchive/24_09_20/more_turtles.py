import turtle

# Setup screen first
screen = turtle.Screen()
screen.setup(1920,1080)

# Save each turtle into a variable
pepa = turtle.Turtle()
vlasta = turtle.Turtle()

# Control each turtle by using its variable
for i in range(100):
    pepa.forward(100)
    vlasta.left(90)

# TODO: Make the turtles have different color
# TODO: Make them walk in random directions (sometimes they turn, sometimes they just go forward)
# TODO: Make the turtles fast