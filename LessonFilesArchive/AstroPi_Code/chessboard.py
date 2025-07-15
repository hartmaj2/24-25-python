# Demonstrates how we can use the color sensor on the Sense HAT and then use that to generate a chessboard pattern
# Link to simulator: https://missions.astro-pi.org/mz/code_submissions/new

from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

width = 8
image = []

b = (0,0,0)

# Use the sensor to read color into s
data = sense.color
s = (data.red,data.green,data.blue)

# Create a chessboard pattern using the color read from the sensor
for i in range(width):
    for j in range(width):
        if (j + i) % 2 == 0:
            image.append(s)
        else:
            image.append(b)

sense.set_pixels(image)