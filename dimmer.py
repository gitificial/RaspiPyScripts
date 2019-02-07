# -*- coding: utf-8 -*-

"""
author: gitificial
date: 07-02-2019

run 
$ sudo python dimmer.py
"""

from gpiozero import *
from time import sleep
# from signal import pause

# extends the PWMOutputDevice
led = PWMLED(27, initial_value = 0.0)
button = Button(17)

directionUp = True

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
				# print("LED value: ", led.value)
				led.value = led.value + 0.01
				sleep(0.1) 
			elif(led.value > 0.99 and led.value <= 1.0):
				led.value = 1.0
				sleep(0.1)

		else:
			# print("directionUp False")
			if(led.value >= 0.01):
				led.value = led.value - 0.01
				sleep(0.1)
			elif(led.value < 0.1 and led.value >= 0.0):
				led.value = 0.0
				sleep(0.1)
