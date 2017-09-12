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

GPIO.output(MotorDir,GPIO.LOW)
GPIO.output(LMotorPwr,GPIO.LOW)
GPIO.output(RMotorPwr,GPIO.LOW)

GPIO.cleanup()

exit()
