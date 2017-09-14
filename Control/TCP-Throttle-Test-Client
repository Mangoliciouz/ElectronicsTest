from time import sleep
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('raspberrypi')
port = 10013
address = (ip, port)
client.connect(address)


# client.send("Hello Server")
# client.recv(1024)

def communicate(data):
    client.send(data.encode())
    reply = client.recv(1024)
    print(reply.decode())
    return


communicate('Engine-100')
sleep(5)
communicate('Engine-0')
sleep(2)
communicate('Disconnect')


exit()
