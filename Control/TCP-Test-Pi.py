import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ip = socket.gethostbyname(socket.gethostname())
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
    if data == 'Hello Server':
        rdata = 'Hello Client'
        client.send(rdata.encode())
        print('    Processing done \n [*] Reply sent')
    elif data == 'Disconnect':
        rdata = 'Goodbye'
        client.Send(rdata.encode())
        client.close()
        break
    else:
        rdata = 'Invalid data'
        client.send(rdata.encode())
        print('    Processing done, Invalid Data \n[*] Reply Sent')

exit()
