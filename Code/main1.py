import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

file = sorted(os.listdir("Images\\Unprocessed"))
files = len(file)
print(file)
r = 0

while r < files:
#Rename
    current = "Images\\Unprocessed\\" + str(file[r])
    renamed = "Images\\Unprocessed\\I"+ str(r) + ".JPG"
    os.rename(current, renamed)

#Crop & BW
    image = Image.open("Images\\Unprocessed\\I" + str(r) + ".JPG").convert("L")
           #left, top, right, bottom
    image = image.crop((33, 950, 3650, 2500))
    plt.imsave("Images\\WIP\\T"+ str(r) + ".JPG", image, cmap="gray")
    #print(r)
    r = r + 1
