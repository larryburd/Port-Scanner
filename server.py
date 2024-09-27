import socket

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# Port to reserve
port = 12345

# Bind port to the created socket
# Not specifying an IP address will default to the current host IP
s.bind(('', port))
print("Socket bind successful")

# Start listening on the socket
# Pass 5 as the backlog parameter to allow 5 requests to be queued
# any requests past the 5th queued one will be dropped/ignored
s.listen(5)

# Create an infinite loop to accept connections
# only terminate it when we interupt or an error occurs
while True:
  # Establish connection with the client
  c, addr = s.accept()
  print('Got connection from ', addr)

  # Send a thank you message to the client with the
  # newly created socket c
  c.send(b'Hello, thank you for connecting')
  msg = c.recv(1024)
  print('The message from the client: ', msg)

  # Close the connection with the client
  c.close()