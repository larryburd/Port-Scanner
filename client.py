import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port number (the same as the server)
port = 12345

# connect to the server on the local computer using the loop-back IP address
s.connect(('127.0.0.1', port))

# Recieve data from the server
print('Server says: ', s.recv(1024))
s.send(b'Hello there')

# Close the connection
s.close()