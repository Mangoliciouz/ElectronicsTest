import socket

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

MotorDirState = "LOW"

LPwr = GPIO.PWM(LMotorPwr,100)
RPwr = GPIO.PWM(RMotorPwr,100)

LPwr.start(0)
RPwr.start(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
ip = '192.168.1.151'
port = 10013
address = (ip, port)
server.bind(address)
server.listen(1)
print('[*] Started listening ', ip,':',port)
(client, addr) = server.accept()
print('[*] Got a connection from ', addr[0],':',addr[1])
while True:
    data = client.recv(32)
    data = data.decode()
    if 'Engine-' in data:
        EPwrNo = data[7:]
        EPwrNo = EPwrNo.rstrip()
        EPwrNo = EPwrNo.lstrip()
        print('[*] Recieved ',EPwrNo,' From the client')
        #rdata = 'Turning Engine to ', filter(type(data).isdigit, data) ,'%'
        #client.send(rdata.encode())
        EPwrNoF = float(EPwrNo)
        LPwr.ChangeDutyCycle(EPwrNoF)
        RPwr.ChangeDutyCycle(EPwrNoF)
        print('    Turning Engine to ', EPwrNo ,'%')
    elif 'Reverse' in data:
        print('[*] Recieved Reverse Throttle Toggle command.')
        if MotorDirState == 'LOW':
            GPIO.output(MotorDir,GPIO.HIGH)
            MotorDirState = 'HIGH'
        else:
            GPIO.output(MotorDir,GPIO.LOW)
            MotorDirState = 'LOW'


    elif data == 'Disconnect':
        rdata = 'Goodbye'
        client.send(rdata.encode())
        client.close()
        print('    Processing done \n[*] Reply sent\n[*] Connection Closed\n[*] Terminating Process')
        break
    else:
        rdata = 'Invalid data'
        client.send(rdata.encode())
        print('    Processing done, Invalid Data \n[*] Reply Sent')

exit()
