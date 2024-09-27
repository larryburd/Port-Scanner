import socket
import json

# Import the port list from the filesystem
with open('ports.lists.json') as f:
  port_list = json.load(f)

# Array of ports that are found to be open
ports_found = []
msgs = []

# Loop through all possible ports
# and add any messages received to the array
for port in range(1, 65535):
  try:
    # Create a socket and attempt to connect to the port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', port))
  except:
    # Ignore exceptions, because that means we couldn't connect
    continue
  else:
    # Append a message for any ports that we can connect to
    ports_found.append(port)

# Add the app descriptions for each open port
# if it exists in the port list JSON file
for p in ports_found:
  try:
    app = port_list[str(p)][0]['description']
  # a keyError tells us the port wasn't found in the JSON list
  except KeyError:
    app = "Unknown"
  
  msgs.append(f"Port {p} is open.  Application: {app}")

for msg in msgs:
  print(msg)