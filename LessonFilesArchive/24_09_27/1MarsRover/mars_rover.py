import turtle

# Mission description at this link: https://www.101computing.net/mars-perseverance-rover/

# TODO: Set path to your images
image_path = "24_09_27/1MarsRover/mars_pics"


mission_images = [1,1,2,3,4,6,5]
mission_start_x = [-165,-165,-165,-165,-155,-165,-35]
mission_start_y = [-165,-165,-167,-169,-135,-165,-160]


# TODO: Set the mission you want to play (1-7)
mission = 1


# Setup screen size and background
screen = turtle.Screen()
screen.setup(410, 410)
screen.bgpic(image_path + "/mars-path-" +str(mission_images[mission - 1]) + ".png")

# Setup rover shape, pen color and pen size
rover = turtle.Turtle()
screen.register_shape(image_path + "/rover.gif")
rover.shape(image_path + "/rover.gif")
rover.color("#810000")
rover.speed(5)
rover.pensize(4)

# Put rover to start possition
rover.penup()
rover.goto(mission_start_x[mission-1],mission_start_y[mission-1])
rover.pendown()

# TODO: Here place your code for rover


screen.mainloop() # keep the program running after the rover stops

# TIPS:
# Close window by Ctrl + C (kill program)
# Make a function for each mission
# Turtle library documentation: https://docs.python.org/3/library/turtle.html#  (Follow link: Cmd + click)
