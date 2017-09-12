#Set Motor Direction to Pin 7 & Power to Pin 8. LOW = Forward

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MotorDir = 10
MotorPwr = 7

GPIO.setup(MotorDir,GPIO.OUT)
GPIO.setup(MotorPwr,GPIO.OUT)

print "Turning Motor on Forwards for 5 Seconds. 0.25 Steps"

sleep(2)

GPIO.output(MotorDir,GPIO.LOW)

Pwr = GPIO.PWM(MotorPwr,100)

Pwr.start(25)

sleep(2)

Pwr.ChangeDutyCycle(50)

sleep(2)

Pwr.ChangeDutyCycle(75)

sleep(2)

Pwr.ChangeDutyCycle(100)

sleep(5)

Pwr.ChangeDutyCycle(75)

sleep(2)

Pwr.ChangeDutyCycle(50)

sleep(2)

Pwr.ChangeDutyCycle(25)

sleep(2)

Pwr.stop()
GPIO.output(MotorPwr,GPIO.LOW)

sleep(2)

print "Turning Motor on backwards for 5 Seconds. 0.25 Steps"

sleep(2)

GPIO.output(MotorDir,GPIO.HIGH)

Pwr = GPIO.PWM(MotorPwr,100)

Pwr.start(25)

sleep(2)

Pwr.ChangeDutyCycle(50)

sleep(2)

Pwr.ChangeDutyCycle(75)

sleep(2)

Pwr.ChangeDutyCycle(100)

sleep(5)

Pwr.ChangeDutyCycle(75)

sleep(2)

Pwr.ChangeDutyCycle(50)

sleep(2)

Pwr.ChangeDutyCycle(25)

sleep(2)

Pwr.stop()

GPIO.output(MotorPwr,GPIO.LOW)

sleep(2)


GPIO.output(MotorDir,GPIO.LOW)

print "Test Complete."

GPIO.cleanup()

sleep(2)

exit()
