import socket
#creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #sock datagram for udp protocols
print('server socket created')
host = 'localhost' #local machine ip
port = 1726
serversocket.bind((host, port)) #socket binding to address
print('server socket connected to ' + host)

message = ' , how are u? =]'
while True:
    data, addr = serversocket.recvfrom(2048) #maximum buffer size of data to be received
    if data:
         print('responding')
         serversocket.sendto(data + (message.encode()), addr)
