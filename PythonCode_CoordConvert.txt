# Convert serially input GPS coordinates to degrees & print output to console
# Ben Christie & Izabella Arredondo

import os
import math
import serial
import sys
import time

# try different ACM ports to connect to Arduino serial
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    if not ser.isOpen():
        ser.open()
except Exception, e:
    print("Error opening port. Quitting." +str(e))

    try:
        ser = serial.Serial('/dev/ttyACM1', 9600)
        if not ser.isOpen():
            ser.open()
    except Exception, e:
        print("Error opening port. Quitting." +str(e))

        try:
            ser = serial.Serial('/dev/ttyACM2', 9600)
            if not ser.isOpen():
                ser.open()
        except Exception, e:
            print("Error opening port. Quitting." +str(e))
        
            sys.exit()

# connect to XBee serial port
try:
    ser1 = serial.Serial('/dev/ttyUSB0', 38400)
    if not ser.isOpen():
        ser.open()
except Exception, e:
    print("Error opening port. Quitting." +str(e))
    sys.exit()
    

# ground station placed at origin
# x = latitude, y = longitude, z = altitude
x1 = 0
y1 = 0
z1 = 0

# spacecraft coordinates
x2 = 1
y2 = 0
z2 = 0

# degree values to set top (2) and bottom (1) servo motors
servo1 = 0
servo2 = 0

# previous degree values combined into one string
prevcomb = 0

# total string value for XBee serial in
total = ''

#run continuously   
while 1:

    # if XBee is available
    if ser1.inWaiting():
        
        # read in serial value
        temp = ser1.read()
        print(temp)

        # if semicolon detected, total input string is complete
        if temp == ';':
            print(total)

            # parse string by commmas
            sx,sy,sz = total.split(',')

            # assign input values to spacecraft coord vals
            x2 = float(sx)
            y2 = float(sy)
            z2 = float(sz)

            # reset total input string 
            total = ''
            
        # else add temp value to total string     
        else:

            total += temp

    # convert lat, long, alt coord vals to degree vals 
    servo1 = math.degrees(math.atan((y2-y1)/(x2-x1)))
    servo2 = math.degrees(math.atan((z2-z1)/(x2-x1)))

    # hard constraints to prevent potentially damaging input to motor
    if servo1 < 0:
        servo1 += 360

    if servo2 < 0:
        servo2 += 360

    if servo2 > 158:
        servo2 = 158

    elif servo2 < 0:
        servo2 = 0

    if servo1 > 180:
            servo1 = servo1 - 180
            servo2 = 180 - servo2
            if servo2 > 158:
                servo2 = 158

    # combine degree vals into one string
    comb = servo1 , servo2

    # if degree string is different than previous,
    # write the val to serial input and assign current to prev
    if comb != prevcomb:
        print(str(comb))
        print(ser.write(str(comb)))
        prevcomb = comb
        
    #time.sleep(1)

    # reset current degree string    
    comb = 0



