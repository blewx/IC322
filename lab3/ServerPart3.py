from socket import *
import sys  # In order to terminate the program

# Define the server port
serverPort = 12346

# Create a TCP socket (IPv4, TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the server address and port
serverSocket.bind(('', serverPort))

# Start listening for incoming connections (maximum 1 connection at a time)
serverSocket.listen(1)

print('The server is ready to serve...')

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    # Receive the request message from the client
    message = connectionSocket.recv(1024).decode()
    print(f"Message received: {message}")

    # Parse the filename from the request
    filename = message.split()[1]
    print(f"Filename requested: {filename}")

    # Open the requested file (remove the leading '/')
    with open(filename[1:], 'r') as f:
        # Read the content of the requested file
        outputdata = f.read()

    # Send the HTTP response header
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

    # Send the content of the file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())

    connectionSocket.close()

# Close the server socket when done (optional, unreachable due to infinite loop)
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
