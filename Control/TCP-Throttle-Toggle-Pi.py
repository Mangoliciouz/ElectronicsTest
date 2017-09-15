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
    data = client.recv(1024)
    print('[*] Recieved ',data,' From the client')
    print('    Proccessing data')

    data = data.decode()
    if data == 'Engine-100':
        rdata = 'Turning Engine to 100%'
        client.send(rdata.encode())
        GPIO.output(LMotorPwr,GPIO.HIGH)
        GPIO.output(RMotorPwr,GPIO.HIGH)
        print('    Processing done \n [*] Reply sent')
    elif data == 'Engine-0':
        rdata = 'Turning Engine Off'
        client.send(rdata.encode())
        GPIO.output(LMotorPwr,GPIO.LOW)
        GPIO.output(RMotorPwr,GPIO.LOW)
        print('    Processing done \n [*] Reply sent')
    elif data == 'Disconnect':
        rdata = 'Goodbye'
        client.send(rdata.encode())
        client.close()
        break
    else:
        rdata = 'Invalid data'
        client.send(rdata.encode())
        print('    Processing done, Invalid Data \n[*] Reply Sent')

exit()
