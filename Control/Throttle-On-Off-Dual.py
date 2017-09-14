#Set Motor Direction to Pin 7 & Power to Pin 8. LOW = Forward

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MotorDir = 10
LMotorPwr = 7
RMotorPwr = 8

GPIO.setup(MotorDir,GPIO.OUT)
GPIO.setup(LMotorPwr,GPIO.OUT)
GPIO.setup(RMotorPwr,GPIO.OUT)

print("Turning Both Motors on Forwards for 5 Seconds.")

sleep(2)

GPIO.output(MotorDir,GPIO.LOW)
GPIO.output(LMotorPwr,GPIO.HIGH)
GPIO.output(RMotorPwr,GPIO.HIGH)

sleep(5)

GPIO.output(LMotorPwr,GPIO.LOW)
GPIO.output(RMotorPwr,GPIO.LOW)

sleep(2)

print("Turning Motor on backwards for 5 Seconds.")

sleep(2)

GPIO.output(MotorDir,GPIO.HIGH)
GPIO.output(LMotorPwr,GPIO.HIGH)
GPIO.output(RMotorPwr,GPIO.HIGH)

sleep(5)

GPIO.output(LMotorPwr,GPIO.LOW)
GPIO.output(RMotorPwr,GPIO.LOW)

sleep(2)

GPIO.output(MotorDir,GPIO.LOW)

print("Test Complete.")

GPIO.cleanup()

sleep(2)

exit()
