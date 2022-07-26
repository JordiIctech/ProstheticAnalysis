import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
import cv2
from numpy import asarray
import os
import csv


rnd = 0
file = sorted(os.listdir("Images\\Corrections"))

while rnd < len(file):
    w1 = []
    h1 = []
    w2 = []
    h2 = []
    wc = []
    hc = []
    t = 0
    flag = 0

    pic = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG")

    width, height = pic.size

    while flag == 0:

        for x in range(1100, width, 1): #The order of these for loops
            for y in range(35, height, 1): #Makes it so that it scans top to bottom and shifts right onece after.
                r, g, b = pic.getpixel((x, y))
                if r in range(170, 245): #and g in range(210, 245) and b in range(210, 245):

                    r, g, b = pic.getpixel((x, y - 5))
                    if r in range(10,100):
                        w1.append(x)
                        h1.append(y)
                        flag = 1
                        break

        for x in range(1100, width, 1): #The order of these for loops
            for y in range(height - 6, 253, -1): #Makes it so that it scans top to bottom and shifts right onece after.

                r, g, b = pic.getpixel((x, y))
                if r in range(190, 245): #and g in range(210, 245) and b in range(210, 245):

                    r, g, b = pic.getpixel((x, y + 5))
                    if r in range(10,185):

                        r, g, b = pic.getpixel((x, y - 5))
                        if r in range(190, 245):
                            w2.append(x)
                            h2.append(y)
                            flag = 1
                            break


    plt.plot(w1, h1)
    plt.gca().invert_yaxis()
    #plt.show()

    plt.plot(w2, h2)
    plt.gca().invert_yaxis()
    #plt.show()

    G2 = Image.open("Images\\Corrections\\C" + str(rnd) + ".JPG")
    G2P = asarray(G2)

    x = 0

    wc = w1 + w2
    hc = h1 + h2
    #print(wc)


    while x < len(wc):
            G2P = cv2.circle(G2P, (wc[x], hc[x]), radius=1, color=(0, 0, 255), thickness=-1)
            x = x + 1

    cv2.imwrite("Images\\Analyzed\\F"+ str(rnd) + ".JPG", G2P)

    wz = []
    hz = []
    ptcm = 121.5789
    for i in range(0,len(w1)):

        wz.append((w1[i] - w1[0])/ptcm)
        hz.append((h1[i] - h1[0])/ptcm)

    z = np.polyfit(w1, h1, 5) # Invert every point's sign to flip curve.
    zz = np.polyfit(w2, h2, 5)

    label = ["x1(2)", "y1(4)", "x2(6)", "y2(8)", "polycurve(10)"]
    BP = [w1, h1, w2, h2, z, zz]

    with open('Images\\Analyzed\\BP' + str(rnd) + ".csv", 'w') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(label)
        write.writerows(BP)

    print(z)
    print(zz)
    print(rnd)
    rnd = rnd + 1