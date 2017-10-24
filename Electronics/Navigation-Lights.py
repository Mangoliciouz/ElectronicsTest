//Controlling Aircraft Led Navigation Lights

import RPi.GPIO as GPIO
from time import sleep

//Turn on GPIO and set Pins

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Fore = 35
Aft = 36
Left = 37
Right = 38
AntiCollision = 40

//Setup GPIO Pins

 GPIO.setup(Fore,GPIO.OUT)
 GPIO.setup(Aft,GPIO.OUT)
 GPIO.setup(Left,GPIO.OUT)
 GPIO.setup(Right,GPIO.OUT)
 GPIO.setup(AntiCollision,GPIO.OUT)

//All Lights On

GPIO.output(Fore,GPIO.HIGH)
GPIO.output(Aft,GPIO.HIGH)
GPIO.output(Left,GPIO.HIGH)
GPIO.output(Right,GPIO.HIGH)


def ACLoop():
    while true:
        GPIO.output(AntiCollision,GPIO.HIGH)
        sleep(1)
        GPIO.output(AntiCollision,GPIO.LOW)
        sleep(1)

def EndLights():
    GPIO.output(Fore,GPIO.LOW)
    GPIO.output(Aft,GPIO.LOW)
    GPIO.output(Left,GPIO.LOw)
    GPIO.output(Right,GPIO.LOW)
    GPIO.output(AntiCollision,GPIO.LOW)
    GPIO.cleanup()

if true();
    try:
        ACLoop()
    except KeyboardInterrupt:
        destroy():

exit()









GPIO.output(AntiCollision,GPIO.HIGH)
