import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
import cv2
from numpy import asarray
import os
import csv
import imutils
import math
from scipy.stats import linregress
import statistics

rnd = 0 # Start Round
file = sorted(os.listdir("Images\\WIP"))  # Get initial Image

while rnd < len(file):  # Setup vectors
    w1 = []
    h1 = []
    w2 = []
    h2 = []
    w3 = []
    h3 = []
    t = 0
    flag = 0

    pic = Image.open("Images\\WIP\\T" + str(rnd) + ".JPG")  # Open image for editing

    width, height = pic.size

    while flag == 0:

        for y in range(125, 500, 1):  # The order of these for loops matters
            for x in range(550, 100, -1):  # Makes it so that it scans top to bottom
                r, g, b = pic.getpixel((x, y))  # Obtains color values for a pixel.
                if r in range(120, 245):  # Compares pixel vs stated color condition

                    r, g, b = pic.getpixel((x - 1, y))
                    if r in range(10, 100):

                        r, g, b = pic.getpixel((x + 1, y))
                        if r in range(120, 245):
                            w1.append(x)
                            h1.append(y)
                            flag = 1
                            break

    mw = statistics.median(w1)

    x = 0                                   # Deletes values far from median of width.
    while x < len(w1):
        if (mw - 20) < w1[x] < (mw + 20):
           x = x + 1
        else:
            del w1[x]
            del h1[x]
            x = x -1

    G2 = Image.open("Images\\WIP\\T" + str(rnd) + ".JPG")    # Open Image
    #G2P = asarray(G2)

    x = 0

    #while x < len(w1):   # Adds Dots
    #    G2P = cv2.circle(G2P, (w1[x], h1[x]), radius=1, color=(255, 0, 0), thickness=2)
    #    x = x + 1

    # cv2.imwrite("Images\\Corrections\\C" + str(rnd) + ".JPG", G2P)  # Saves Dots

    #pic = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG")  # Opens Image with Dots


    slope, intercept, r_value, p_value, std_err = linregress(h1, w1)  # Get line values for vertical line.


    ang = math.degrees(math.atan((slope - 0) / (1 + 0 * slope)))   # Angle Calculations

    Roti = pic.rotate(ang*-1)  # Rotate Picture.

    Roti.save("Images\\Corrections\\C" + str(rnd) + ".JPG") # Saves rotation.

    pic = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG") # Reopens saved image.

    for x in range(150, 900, 1):  # Getting Values for Horizontal Line
        for y in range(350, 100, -1):

            r, g, b = pic.getpixel((x, y))
            if r in range(160, 245):

                r, g, b = pic.getpixel((x, y - 4))
                if r in range(10, 155):

                    r, g, b = pic.getpixel((x, y + 4))
                    if r in range(155, 245):
                        w2.append(x)
                        h2.append(y)
                        flag = 1
                        break


# ----------------------------------------------------------------------------------------------------------------------

 # Reobtaining the horizontal slope
    flag = 0
    while flag == 0:
        for y in range(150, 500, 1):  # The order of these for loops
            for x in range(550, 100, -1):  # Makes it so that it scans top to bottom and shifts right once after.
                r, g, b = pic.getpixel((x, y))
                if r in range(120, 245):  # and g in range(210, 245) and b in range(210, 245):

                    r, g, b = pic.getpixel((x - 1, y))
                    if r in range(10, 100):

                        r, g, b = pic.getpixel((x + 1, y))
                        if r in range(120, 245):
                            w3.append(x)
                            h3.append(y)
                            flag = 1
                            break

    mw = statistics.median(w3)

    x = 0

    while x < len(w3):
        if (mw - 20) < w3[x] < (mw + 20):
           x = x + 1
        else:
            del w3[x]
            del h3[x]
            x = x -1

    slope, intercept, r_value, p_value, std_err = linregress(h3, w3)

    #G2 = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG")
    #G2P = asarray(G2)

    x = 0

    #while x < len(w3):
    #    G2P = cv2.circle(G2P, (w3[x], h3[x]), radius=1, color=(0, 255, 0), thickness=2)
    #    x = x + 1

   # cv2.imwrite("Images\\Corrections\\C" + str(rnd) + ".JPG", G2P)

 # -------------------------------------------------------------------------------------------------


    mh = statistics.median(h2) # Analysis for previous horizontal line
    x = 0
    while x < len(h2):
        if (mh - 5) < h2[x] < (mh + 5):
           x = x + 1
        else:
            del w2[x]
            del h2[x]
            x = x - 1


   # G2 = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG")
   # G2P = asarray(G2)

    x = 0
    # while x < len(w2):
    #    G2P = cv2.circle(G2P, (w2[x], h2[x]), radius=1, color=(0, 0, 255), thickness=2)
    #    x = x + 1

    # cv2.imwrite("Images\\Corrections\\C" + str(rnd) + ".JPG", G2P)

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(h2, w2) # Horizontal line values.

    mx = statistics.median(w3)
    my = statistics.median(h2)


    FILE_NAME = 'volleyball.jpg'
    # Create translation matrix.
    M = np.float32([[1, 0, 100 - mx ], [0, 1, 100 - my]]) # Let's shift by (100, 50).

    # Read image from disk.
    img = cv2.imread("Images\\Corrections\\C" + str(rnd) + ".JPG")
    (rows, cols) = img.shape[:2]

    # warpAffine does appropriate shifting given the
    # translation matrix.
    res = cv2.warpAffine(img, M, (cols, rows))

    # Write image back to disk.
    cv2.imwrite("Images\\Corrections\\C" + str(rnd) + ".JPG", res)

    print(rnd)
    rnd = rnd + 1