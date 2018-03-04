# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:38:37 2018

@author: Patrick
"""

import serial
import time


ser = serial.Serial('COM3', 115200)  # open serial port
print(ser.name)         # check which port was really used


#for i in range(10):    
ser.write(b'hello\0')     # write a string
#time.sleep(0.1)
#st = ser.read(6)
#    
#print(st)
ser.close()             # close port4r