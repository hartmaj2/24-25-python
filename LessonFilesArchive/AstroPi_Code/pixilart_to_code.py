# This program converts a png pixelart of n*n size to code for Astro Pi challenge
# Link to simulator: https://missions.astro-pi.org/mz/code_submissions/new
# Link to pixilart: https://www.pixilart.com/draw

# How to use this script
# 1. Create new image in pixilart, choose 8x8 dimensions
# 2. Download the image as .png (Download -> Download .png)
# 3. Run this script

from PIL import Image
import os
import math

INPUT_FILENAME = "pixil.png"

# get an array of pixels, each pixel is a tuple (red,green,blue)
def get_color_array(filename : str) -> list[tuple]:
    output_bmp = "temp.bmp"
    img = Image.open(filename)
    img.save(output_bmp)
    img = Image.open(output_bmp)
    bytes = img.tobytes()
    os.remove(output_bmp)
    pixels = []
    for i in range(0,len(bytes),3):
        pixel = (bytes[i], bytes[i+1], bytes[i+2])
        pixels.append(pixel)
    return pixels

# initializes a dict that stores the variable name for each color we are using in the picture
def get_col_to_var_dict(pixels : list[tuple]) -> dict[tuple,str]:
    current_var = ord('a')
    col_to_var = {}
    for pixel in pixels:
        if pixel not in col_to_var:
            col_to_var[pixel] = chr(current_var)
            current_var += 1
    return col_to_var

# prints variable declarations of the colors we will use
def print_vars_string(col_to_var_dict : dict[tuple,str]):
    for key,value in zip(col_to_var_dict.keys(),col_to_var_dict.values()):
        print(f"{value} = {key}")

# assume the image is a square grid
def print_image_list(pixels : list[tuple], var : dict[tuple,str]):
    sep = ","
    width = int(math.sqrt(len(pixels)))
    print(f"image = [")
    for i in range(width):
        vars = [var[px] for px in pixels[width*i:width*(i+1)]]
        print(f"\t{sep.join(vars)}",end="")
        if i != width - 1:
            print(sep)
        else:
            print("]")

pixels = get_color_array(INPUT_FILENAME)
col_to_var = get_col_to_var_dict(pixels)
print_vars_string(col_to_var)
print_image_list(pixels,col_to_var)