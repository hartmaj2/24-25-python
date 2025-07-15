# This program demonstrates how we can loop through multiple images in SenseHat AstroPi mission simulation
# Link to simulator: https://missions.astro-pi.org/mz/code_submissions/new

from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
a = (255, 255, 255) # White
c = (0, 0, 0) # Black
f = (25, 25, 112) # MidnightBlue
m = (34, 139, 34) # ForestGreen
t = (255, 140, 0) # dark orange
b = (105, 105, 105) # DimGray
d = (100, 149, 237) # CornflowerBlue
v = (255, 0, 0) # Red
z = (153, 50, 204) # DarkOrchid

# Set up the images
image1 = [
  m, m, m, m, m, c, c, c,
  m, f, m, f, m, m, m, m,
  m, m, m, m, m, m, m, m,
  m, m, c, a, c, c, c, a,
  m, m, c, c, c ,c ,c ,c,
  m, m, c, c, c, a, c, c,
  m, m, m, m, m, m, m, m,
  m, m, m, m, m, m, m, m]

image2 = [
  t, a, t, c, c, t, a, t,
  t, a, t, c, c, t, a, t,
  t, t, t, t, t, t, t, t,
  t, a, c, t, t, c, a, t,
  t, t, t, t, t, t, t, t,
  a, a, a, c, c, a, a, a,
  c, a, a, a, a, a, a, c,
  c, c, a, a, a, a, c, c]

image3 = [
  c, c, v, c, v, c, c, c,
  c, z, z, z, z, v, c, c,
  z, b, z, b, z, c, c, c,
  z, z, z, z, z, v, c, c,
  c, c, d, d, d, c, c, z,
  c, z, d, z, z, z, z, c,
  c, c, d, d, z, c, c, c,
  c, c, z, c, z, c, c, c]

images = [image1, image2, image3]

# Loop through the images
for image in images:
  sense.set_pixels(image)
  sleep(1)