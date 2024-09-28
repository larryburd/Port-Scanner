import socket
import json
from os.path import exists

port_list_filepath = 'ports.lists.json'
port_list = []

# Check if the port list file exists
if exists(port_list_filepath):
  # Import the port list from the filesystem
  with open(port_list_filepath) as f:
    port_list = json.load(f)
else:
  print('PORT LIST NOT FOUND IN CURRENT FOLDER')
  print('ALL PORT APPLICATIONS WILL BE LISTED AS UNKOWN')

# Arrays of ports that are found to be open and messages for printing
ports_found = []
msgs = []

# PRIMARY SYSTEM LOGIC
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
    if len(port_list) > 0:
      app = port_list[str(p)][0]['description']
    else:
      app = "Unknown"
  # a KeyError tells us the port wasn't found in the JSON list
  except KeyError:
    app = "Unknown"
  
  msgs.append(f"Port {p} is open.  Application: {app}")

for msg in msgs:
  print(msg)