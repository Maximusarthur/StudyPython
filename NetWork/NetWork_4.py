#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('10.100.59.169', 6789))
serverSocket.listen(1)
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = 'hello.html'
        f = open(filename, encoding='utf-8')
        outputdata = f.read().encode()
        #Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n' % len(outputdata)
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        for i in range(len(outputdata)):
            connectionSocket.send(bytes([outputdata[i]]))
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()
serverSocket.close()
