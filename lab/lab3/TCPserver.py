
from socket import *
serverPort = 12346 
serverSocket = socket (AF_INET, SOCK_STREAM) 
serverSocket. bind(('' ,serverPort) ) 
serverSocket. listen (1) 
print ('The server is ready to receive') 
while True: 
    connectionSocket, addr = serverSocket.accept() 
    sentence = connectionSocket.recv(1024).decode() 
    capitalizedSentence = sentence.upper() 
    message = "Let's make this upper case \n" 
    #m = "<html><body>Hello, world!</body></html>\n"
    print(sentence)
    response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 39\r\n\r\n<html><body>Hello, world!</body></html>"""
    connectionSocket.send(response.encode())
    #connectionSocket.send(m.encode())
    #connectionSocket.send(capitalizedSentence.encode()) 
    connectionSocket.close()
