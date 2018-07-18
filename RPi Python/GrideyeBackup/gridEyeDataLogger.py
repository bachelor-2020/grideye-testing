# -*- coding: utf-8 -*-
from  GridEyeKit import GridEYEKit
import time
import numpy as np
from sys import exit
import os

#open a text file to read to
print("Connecting to Grideye\n")
try:
    f = open('dataFile.csv','a')
except:
    print("failed to open file %s" % f)
try:
    g = GridEYEKit()
    g_status_connect = g.connect()
    if not g_status_connect:
        g.close()
        f.close()
        print("could not connect to grideye...\n")
        os._exit(1)
    print("Connected\n")
except:
    print("could not connect to grideye...\n")
    g.close()
    f.close()
    os._exit(1)


while(1):
    #get an 8x8 matrix (2d list)
    data = g.get_temperatures()
    #print(g.get_thermistor())
    #time stamp of current time (only in seconds atm)
    time_stamp = [time.ctime()]
    #flatten 8x8 matrix into legnth 64 list os strings,
    #element 0 is top left, element 63 bottom right
    data = data.flatten()
    data = map(str,data)
    rowData = time_stamp+data
    rowData = '"'+'","'.join(rowData)+'"\n'
    #write to the csv file
    #column 2:65 is grideye pixel data
    f.write(rowData)
    #pause for a tenth of a second
    time.sleep(0.1)
g.close()
f.close()
