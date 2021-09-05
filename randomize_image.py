from PIL import Image
from random import randint
import random
import os

def full_random_image():

    image_name = random.choice(os.listdir("images"))
    asset_image = Image.open("images/"+image_name)

    asset_size = asset_image.size
    base_size = (asset_size[0]+100,asset_size[1]+100)
    base_image = Image.new(mode="RGB", size=base_size, color=(0,0,0,0))
    base_image.paste(asset_image, (50,50), mask=asset_image)

    u_colors = asset_image.getcolors()

    pixels = base_image.load() # create the pixel map
    no_change = []

    for color in u_colors:
        if color[1][3] > 0:
            color_c = (color[1][0],color[1][1],color[1][2])
            if color_c not in no_change:
                rand_color = (randint(0,255),randint(0,255),randint(0,255))
                for i in range(base_image.size[0]): # for every pixel:
                    for j in range(base_image.size[1]):
                        if pixels[i,j] == color_c:
                            pixels[i,j] = rand_color
            

    base_mask = Image.new(mode="RGB", size=base_size, color=(0,0,0,0))
    base_mask.putalpha(0)
    base_mask.paste(asset_image, (50,50), mask=asset_image)
    
    return((base_image,base_mask))

def random_color_image(image_name):

    asset_image = Image.open("images/"+image_name)

    asset_size = asset_image.size
    base_size = (asset_size[0]+100,asset_size[1]+100)
    base_image = Image.new(mode="RGB", size=base_size, color=(0,0,0,0))
    base_image.paste(asset_image, (50,50), mask=asset_image)

    u_colors = asset_image.getcolors()

    pixels = base_image.load() # create the pixel map
    no_change = []

    for color in u_colors:
        if color[1][3] > 0:
            color_c = (color[1][0],color[1][1],color[1][2])
            if color_c not in no_change:
                rand_color = (randint(0,255),randint(0,255),randint(0,255))
                for i in range(base_image.size[0]): # for every pixel:
                    for j in range(base_image.size[1]):
                        if pixels[i,j] == color_c:
                            pixels[i,j] = rand_color
            

    base_mask = Image.new(mode="RGB", size=base_size, color=(0,0,0,0))
    base_mask.putalpha(0)
    base_mask.paste(asset_image, (50,50), mask=asset_image)
    
    return((base_image,base_mask))
