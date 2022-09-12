import cv2.cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
import cv2
from numpy import asarray
import os
import csv

# ----------------------------------------------------- Import numbers from dataanalysis
rnd = 0
file1 = sorted(os.listdir("Images\\Analyzed"))
file2 = sorted(os.listdir("Images\\Corrections"))
B = 40
G = 0 # 255 is max
R = 0

while rnd < (len(file1)//2):
    with open("Images\\Analyzed\\BP" + str(rnd) + ".csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    del data[0]

# -------------------------------------------------------------------------------- Make numbers usable
    x = 0
    while x < len(data):  #Delete empty spaces

        if not data[x]:
            del data[x]

        else:
            x = x + 1

    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]

    for i in range(0, len(x1)):  # Make strings into integers
        x1[i] = int(x1[i])

    for i in range(0, len(y1)):
        y1[i] = int(y1[i])

    for i in range(0, len(x2)):
        x2[i] = int(x2[i])

    for i in range(0, len(y2)):
        y2[i] = int(y2[i])

    print(len(x1))
    print(len(y1))
    print(x1)
    print(y1)
    print(len(x2))
    print(len(y2))
    print(x2)
    print(y2)
    print(len(data))
    print(data)

# ------------------------------------------------------------ Reduce points for rectangles

    if len(x1) > len(x2):  # Makes it so xr1 is always largest array.
        xr1 = x1
        yr1 = y1
        xr2 = x2
        yr2 = y2

    else:
        xr1 = x2
        yr1 = y2
        xr2 = x1
        yr2 = y1

    print(len(xr1))
    print(len(xr2))
    print(xr1)

    for i in range(len(xr1)-1, 0, -1):  # Starts from the end
        if xr1[i] not in xr2:
            del xr1[i]
            del yr1[i]
    print(len(xr1))
    print(len(xr2))
    print(xr1)

    for i in range(len(xr2)-1, 0, -1):  # Starts from the end
        if xr2[i] not in xr1:
            del xr2[i]
            del yr2[i]
    print(len(xr1))
    print(len(xr2))
    print(xr1)
    print(yr1)
    print(xr2)
    print(yr2)

    # ----------------------------------------------------------- Make rectangles

    image = cv2.imread("Images\\Corrections\\C" + str(rnd) + ".JPG")

    colorC = 1020  # 255 per color, want from green to red to green to 255 * 3
    listlen = len(xr1)
    listunit = colorC/listlen # Change in R G B combined is the division.
    G = 255
    R = 0
    stage = 0

    for i in range(len(xr1)):              # Define Colors

       # if R < 255 and G == 255:
        if stage == 0:
            R = R + listunit
            print("One")
            if R >= 255:
                R = 255
                stage = stage + 1

        elif stage == 1:
            G = G - listunit
            print("Two")
            if G <= 0:
                G = 0
                stage = stage + 1

        elif stage == 2:
            G = G + listunit
            print(G)
            if G >= 255:
                G = 255
                stage = stage + 1

        elif stage == 3:
            R = R - listunit
            if R <= 0:
                R = 0
                stage = stage + 1

        imageM = cv2.rectangle((image), (xr1[i],yr1[i]), (xr2[i],yr2[i]), (B*0.9, G*0.9, R*0.9), thickness=cv2.FILLED) # B G R

    cv2.imwrite(("Images\\Visual\\V" + str(rnd) + ".JPG"), imageM)
    rnd = rnd + 1
    print("Round: " + str(rnd))
