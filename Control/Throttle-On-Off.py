#Set Motor Direction to Pin 7 & Power to Pin 8. LOW = Forward

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MotorDir = 7
MotorPwr = 8

GPIO.setup(MotorDir,GPIO.OUT)
GPIO.setup(MotorPwr,GPIO.OUT)

print "Turning Motor on Forwards for 5 Seconds."

sleep(2)

GPIO.output(MotorDir,GPIO.LOW)
GPIO.output(MotorPwr,GPIO.HIGH)

sleep(5)

GPIO.output(MotorPwr,GPIO.LOW)

sleep(2)

print "Turning Motor on backwards for 5 Seconds."

sleep(2)

GPIO.output(MotorDir,GPIO.HIGH)
GPIO.output(MotorPwr,GPIO.LOW)

sleep(5)

GPIO.output(MotorPwr,GPIO.LOW)

sleep(2)

GPIO.output(MotorDir,GPIO.LOW)

print "Test Complete."

GPIO.cleanup()

sleep(2)

exit()
