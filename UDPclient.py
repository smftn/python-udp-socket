import socket
#creating socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #sock datagram for udp protocols
print('server socket created')
host = 'localhost' #local machine ip
port = 1726
message = 'hello'
try:
    print('client: ' + message)
    clientsocket.sendto(message.encode(), (host, 1726))
    data, server = clientsocket.recvfrom(2048)
    data = data.decode()
    print('server: ' + data)

finally:
    print('closing client socket')
    clientsocket.close()
