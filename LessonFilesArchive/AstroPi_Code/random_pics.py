# Loops through given number of randomly generated images (each pixel color is chosen uniformly at random)
# Link to simulator: https://missions.astro-pi.org/mz/code_submissions/new

from sense_hat import SenseHat
import time
import random

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

r = (255,0,0)
d = (0,0,0)

grid_width = 8

def get_random_image():
    image = []
    for i in range(grid_width**2):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        image.append((r,g,b))
    return image

# Add colour variables and image

reps = 5
for i in range(reps):
    sense.set_pixels(get_random_image())
    time.sleep(1)