# All necesarry libraries imported
# For getaddr()
import requests, json

# For connect() and server
import socket

# For connect()
import time

# ----------------------------------------------------
# getaddr() function | Gets current public ipv4 address
# Code courtesy of pytutorial

def getaddr():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    # Error code handling
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()
    # Return ip address field of response.json
    return response.json()['ip']


# ----------------------------------------------------
# connect() algorithm | Connects client to game host

pubaddress = '' # Insert the public ipv4 address of the host
pubport = int() # Insert the port of the host

def connect():
    count = 1
    while True:
        print(f"Attempting to establish a connect to host. Attempt nr. {count}")
        try:
            sock.connect((pubaddress,pubport))
            # Getting address may be used later if a P2P design is employed
            # print("Connection established!")
            # addr = getaddr()
            # print(addr)
            break
        except:
            time.sleep(5)
            count += 1
            continue


# ----------------------------------------------------
# Server() function for incomming connections
def server():
    # IP address and port must be specified
    localip = '' # Insert local ipv4 address of host
    localport = int() # Insert internal port of host
    
    # A socket is assigneed to the sock variable. The socket is then bound to the host on selected port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((localip, localport))
    
    # The socket also has a maximum incomming request cue set to 3
    sock.listen(3)
    
    # The socket will then infinitely listen for incomming connections.
    while True:
        clientsocket, address = sock.accept()
        # Print statement and message is good for debugging but should be removed in final release
        print(f"Connection from {address} has been established.")
        clientsocket.send(bytes("Hey there!!!","utf-8"))



# ----------------------------------------------------
# Outgoing socket | Client behaviour

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect()
msg = sock.recv(1024)
print(msg.decode("utf-8"))
