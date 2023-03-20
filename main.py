'''
created by Jonas Schmidt on 3/19/2023
'''
from PIL import Image

im = Image.open("rubiks_cube.jpg")

im = im.convert("RGBA")

dim = im.size

for x in range(dim[0]):
    for y in range(dim[1]):
        if(im.getpixel((x, y))[0] > im.getpixel((x, y))[1] and im.getpixel((x, y))[0] > im.getpixel((x, y))[2]):
            print("r")
            im.putpixel((x, y), (255, 0, 0, 255))

        elif(im.getpixel((x, y))[1] > im.getpixel((x, y))[2]):
            print("g")
            im.putpixel((x, y), (0, 255, 0, 255))

        else:
            print("b")
            im.putpixel((x, y), (0, 0, 255, 255))

im.save("result.png", format="png")

