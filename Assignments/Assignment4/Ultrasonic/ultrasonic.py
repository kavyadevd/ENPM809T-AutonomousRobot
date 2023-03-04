'''
Copyright (c) 2023 Kavyashree Devadiga
@file       ultrasonic.py
@brief      Reads distance of a immobile object using ultrasonic sensor on RPi
@license    This project is released under the BSD-3-Clause license.
'''

import RPi.GPIO as gpio
import time
import os
import cv2
import numpy as np

trig = 16 # Trigger pin connected to pin 16 on Rpi (GPIO23)
echo = 18 # Echo pin connected to pin 18 on Rpi (GPIO24)


def get_distance():
    ''' Returns distance read from ultrasonic sensor '''
    gpio.setmode(gpio.BOARD)
    gpio.setup(trig, gpio.OUT)
    gpio.setup(echo, gpio.IN)

    # Output = No value
    gpio.output(trig, False)
    time.sleep(0.0001)

    # Generate Trigger:
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    # Generate Trigger:
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    # Generate echo time signal:
    while gpio.input(echo) == 0:
        pulse_start = time.time()
    while gpio.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Time to Distance: (Time*2*Speed of sound)
    distance = round(pulse_duration*17150, 2)

    # Clean gpio pins & return distance
    gpio.cleanup()
    return distance


if __name__ == '__main__':
    distances = []
    ## Get 10 reading to calculate average
    for i in range(10):
        curr_distance = get_distance()
        distances.append(curr_distance)
        print(f"{i}.) Distance : {curr_distance} ")
    average = np.average(curr_distance) ## Average distance
    
    ## Capture image using Rpi camera
    os.system('raspistill -w 640 -h 480 -o Detected_Distance.jpg')

    ## Read and put Text with distance on captured image
    txt2 = f"{average:.3f}"
    print("Average Distance of Jenga box is: ", txt2)
    img = cv2.imread('Detected_Distance.jpg')
    img = cv2.putText(img, "Average Distance of Jenga box is: ", (77, 40),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2, cv2.LINE_AA)
    img = cv2.putText(img, txt2, (88, 70), cv2.FONT_HERSHEY_SIMPLEX,
                      1, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Distances of box ", img)
    cv2.waitKey(0)

    cv2.imwrite("Detected_Distance_Avg.jpg", img)
