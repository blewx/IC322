
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
    print(sentence) 
    connectionSocket.send(message.encode ()) 
    connectionSocket.send(capitalizedSentence.encode()) 
    connectionSocket.close()
