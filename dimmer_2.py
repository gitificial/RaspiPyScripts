# -*- coding: utf-8 -*-

"""
author: gitificial
date: 27-03-2019

run 
$ sudo python dimmer_2.py
"""

from gpiozero import *
from time import sleep
# from signal import pause

# extends the PWMOutputDevice
led = PWMLED(27, initial_value = 0.0)
button = Button(17)

directionUp = False

def changeDirection():
	# search for variable in global scope
	global directionUp
	if(directionUp == True):
		directionUp = False
	else:
		directionUp = True

# function to run, when the button changes the state from inactive to active
button.when_pressed = changeDirection

while(True):
    if(button.is_pressed):
    # print("Button pressed")
        if(directionUp == True):
        # print("directionUp True")
            if(led.value <= 0.99):
                led.value = float(format((led.value + 0.01), '.2f'))
                # print(led.value)
                sleep(0.1) 
            else:
                pass

        else:
            # print("directionUp False")
            if(led.value >= 0.01):
                led.value = float(format((led.value - 0.01), '.2f'))
                # print(led.value)
                sleep(0.1)
            else:
                pass
