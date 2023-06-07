# Throughout this file two parties will be referred to: "host" and "client"
# "Host" refers to the player running the server.
# "Client" refers to the player communicating with the host's game server

# All networking in this program is built on the socket library
# time library is required to wait a bit before attempting to reconnect to host
import socket, time

# Network attempt count is defined and starts at one
count = 1

# User is prompted for the ip address and port of host
pubaddress = str(input("Please input public ipv4 address of host: "))
pubport = int(input("Please input the port of the host: "))

# Creates socket object named "host" using ipv4 and TCP
host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client will attempt to connect indefinitely to host until a connection has
# successfully been established
while True:
    print(f"Attempting to establish a connect to host. Attempt nr. {count}")
    try:
        # If client succesfully connects, loop breaks
        host.connect((pubaddress,pubport))
        print("Connection to host successfully established!")
        break
    except:
        # If client fails to connect the loop is briefly paused, and the client retries
        # with an updated attempt count
        time.sleep(5)
        count += 1
        continue

def selection():
    print("Awaiting host's move")
    # Await client's move while host chooses their own
    hostmove = host.recv(1024)
    hostmove = hostmove.decode('utf-8')
    print(hostmove)
    print("The host has selected a move")
    
    while True:
        # Prompt client for move
        clientmove = str(input(f"Please choose your move (Rock, Paper, or Scissors): "))
        # If host selects an invalid move, prompt a redo
        if clientmove not in moveset:
            print("You have selected a nonexistent move. Remember the move must be capitalised")
            continue
        else:
            clientmove = moveset[clientmove]
            break
        # If client selects an appropriate move convert it to the corisponding number,
        # and transmit client number
    try:
        host.send(bytes(str(clientmove),'utf-8'))
        print("Move registered")
        home()
    except:
        print("Move transmission error")
    return()

def victor():
    winner = host.recv(1024)
    print(winner.decode('utf-8'))
    retry = input("Would you like to play again (y/n)?: ")
    
    if retry == "y":
        host.send(bytes(retry,'utf-8'))
    else:
        host.send(bytes(retry,'utf-8'))
    return()

def home():
    while True:
        command = host.recv(1024)
        command = command.decode('utf-8')
        if command == "moveselect":
            selection()
        elif command == "victor":
            victor()
        elif command == "noreplay":
            noreplay()
    return()

def noreplay():
    print("Unfortunately the host has declined a rematch")
    print("Thank you for playing!")
    host.close()
    exit()

moveset = {
        "Rock":int(0),
        "Paper":int(1),
        "Scissors":int(2),
        }

#commandbook = {
#        "moveselect":selection(),
#        "noreplay":noreplay(),
#        }

home()
