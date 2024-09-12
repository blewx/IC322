
from socket import *
import sys  # In order to terminate the program

# Define the server port
serverPort = 12000

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

    try:
        # Receive the request message from the client
        message = connectionSocket.recv(1024).decode()
        print(f"Message received: {message}")

        # Parse the filename from the request
        filename = message.split()[1]
        print(f"Filename requested: {filename}")

        # Check the file extension to handle images or text
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Open the image file in binary mode
            with open(filename[1:], 'rb') as f:
                outputdata = f.read()

            # Send the HTTP response header for images
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/jpeg\r\n\r\n".encode())
        else:
            # Open text file in text mode (remove leading '/')
            with open(filename[1:], 'r') as f:
                outputdata = f.read().encode()

            # Send the HTTP response header for text files
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

        # Send the content of the file to the client
        connectionSocket.send(outputdata)

    except IOError:
        # Send a 404 Not Found response if the file is not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

    # Close the client connection
    connectionSocket.close()

# Close the server socket when done (optional, unreachable due to infinite loop)
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
