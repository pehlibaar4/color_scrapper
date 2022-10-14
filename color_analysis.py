# %%
import math
from PIL import Image, ImageStat
import random
import csv

# %%
image_file = r"E:\docs\Canva_Colors\assets\pexels-1.jpg"
color_file = r"E:\docs\Canva_Colors\Canva_pallettes.csv"

# %%
def image_brightness( image_file ):
   """https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python"""
   im = Image.open(image_file)
   stat = ImageStat.Stat(im)
   r,g,b = stat.mean
   image_brightness =  math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
   brightness_percentage = round((image_brightness / 255) * 100)
   print(f"Image Brightness: {brightness_percentage}")
   return brightness_percentage

# %%
def hex_to_RGB(hex):
    hex = hex.lstrip('#')
    RGB_value = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return RGB_value

# %%
# Luminance calculation
def find_color_brightness(color_RGB):
    R, G, B = color_RGB[0], color_RGB[1], color_RGB[2]
    luminance = round((0.2126 * R) + (0.7152 * G) + (0.0722 * B))
    color_brightness = round((luminance / 255) * 100)   # percentage
    return color_brightness


# %%
def choose_random(list):
    random.shuffle(list)
    item = random.choice(list)
    return item

# %%
# RGB to HEX
def RGB_to_HEX(color_RGB):
    color_HEX = "#%02x%02x%02x" % color_RGB
    return color_HEX 

# %%
def color_brightness_range( min, max, color_HEX ):
    color_RGB = hex_to_RGB(color_HEX)
    color_brightness = find_color_brightness(color_RGB)
    # print(f"Brightness: {color_brightness}")
    if color_brightness >= min and color_brightness <= max:
        return True

# %%
def primary_secondary_range(image_brightness):
    if image_brightness >= 0 and image_brightness <= 25:
        primary_min, primary_max = 50, 75
        secondary_min, secondary_max = 50, 100

    if image_brightness >= 25 and image_brightness <= 50:
        primary_min, primary_max = 75, 100
        secondary_min, secondary_max = 50, 100

    if image_brightness >= 50 and image_brightness <= 75:
        primary_min, primary_max = 25, 50
        secondary_min, secondary_max = 0, 50

    if image_brightness >= 75 and image_brightness <= 100:
        primary_min, primary_max = 25, 50
        secondary_min, secondary_max = 0, 50

    return primary_min, primary_max, secondary_min, secondary_max

# %%
def find_primary_secondary_color(image_brightness, pallette_list):
    primary_min, primary_max, secondary_min, secondary_max = primary_secondary_range(image_brightness)
    
    selected_pallette = choose_random(pallette_list)
    # print(f"Selected Pallette: {selected_pallette}")

    primary_color = None
    secondary_color = None

    for color in selected_pallette:
        # print(f"For primary : {color}")
        if color_brightness_range(primary_min, primary_max, color):
            primary_color = selected_pallette.pop(selected_pallette.index(color))
            # print(f"After primary color: {selected_pallette}")

        if primary_color:
            for color in selected_pallette:
                # print(f"For secondary : {color}")
                if color_brightness_range(secondary_min, secondary_max, color):
                    secondary_color = selected_pallette.pop(selected_pallette.index(color))
                    # print(f"After secondary color: {selected_pallette}")

                if primary_color and secondary_color:
                    print(f"primary_color: {primary_color}, secondary_color: {secondary_color}")
                    return primary_color, secondary_color

    return find_primary_secondary_color(image_brightness, pallette_list)
                        

# %%
pallette_list = []
with open(color_file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        color_string = [row[0], row[1], row[2], row[3]]
        pallette_list.append(color_string)
        # print(color_string)

# # %%
# image_brightness = image_brightness( image_file )

# # %%
# primary_color, secondary_color = find_primary_secondary_color(image_brightness, pallette_list)

# # %%
# primary_color

# # %%
# secondary_color


