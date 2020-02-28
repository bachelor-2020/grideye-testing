# -*- coding: utf-8 -*-
from  GridEyeKit import GridEYEKit
import time
import numpy as np
import os
import matplotlib.pyplot as plt

print("Connecting to Grideye\n")
try:
    g = GridEYEKit()
    g_status_connect = g.connect()
    if not g_status_connect:
        g.close()
        print("could not connect to grideye...\n")
        os._exit(1)
    print("Connected\n")
except:
    print("could not connect to grideye...\n")
    g.close()
    os._exit(1)


while(1):
    #get an 8x8 matrix (2d list)
    data = g.get_temperatures()

    #Plot the temperature data
    plt.imshow(data, vmin=20, vmax=30)
    plt.show(block=False)
    plt.draw()
    plt.pause(0.1)
g.close()
