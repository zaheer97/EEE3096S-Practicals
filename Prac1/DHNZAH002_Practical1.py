#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Dhunny Zaheer>
Student Number: <DHNZAH002>
Prac: <Prac 1>
Date: <22/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from itertools import product
# Logic that you write
z = 0 #initialise index/counter to zero
list1 = list(product([0,1],repeat = 3)) # creating a double array with all possible permuatations of 0 and 1
def main():
    global z # make variable z global so that we can modify if outside of the current scope
    #the double array is indexed at index z to obtain a single array
    GPIO.output(4,list1[z][0]) #sets the ouput to the first value in the array
    GPIO.output(17,list1[z][1]) #sets the ouput to the second value in the array
    GPIO.output(27,list1[z][2]) #sets the ouput to the third value in the array

GPIO.setmode(GPIO.BCM) #use the pinout for BCM
GPIO.setwarnings(False) #disable warnings
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) #GPIO pin 23 is set up as an input, pulled up, connected to ground on button pressed
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) #GPIO pin 24 is set up as an input, pulled up, connected to ground on button pressed
GPIO.setup(4, GPIO.OUT) #GPIO pin 4 is set up as an output
GPIO.setup(17, GPIO.OUT) #GPIO pin 17 is set up as an output
GPIO.setup(27, GPIO.OUT) #GPIO pin 27 is set up as an output


#threaded callback function for falling egde event on GPIO pin 23
def my_callback(channel):
    global z
    if z >= 7: #when index of array exceeds the last index(7), the index is set to zero to make a loop
       z = 0
    else:
       z += 1 #increments the index/counter by 1

#threaded callback function for falling egde event on GPIO pin 24
def my_callback2(channel):
    global z
    if z <= 0: #when index of array becomes less than the first index(0), the index is set to seven to make a loop
       z = 7
    else:
       z -= 1 #decrements the index/counter by 1

#when a falling edge is detected(button is pressed) on GPIO pin 23, the function my_callback will be run
#bouncetime = 300 is the bounce control. It sets 300 ms during which second button press will be ignored
GPIO.add_event_detect(23, GPIO.FALLING, callback = my_callback, bouncetime = 300)

#when a falling edge is detected(button is pressed) on GPIO pin 24, the function my_callback2 will be run
GPIO.add_event_detect(24, GPIO.FALLING, callback = my_callback2, bouncetime = 300)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
           main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
