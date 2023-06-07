# Throughout this file two parties will be referred to: "host" and "client"
# "Host" refers to the player running the server.
# "Client" refers to the player communicating with the host's game server

# All networking in this program is built on the socket library
import socket
from pubip import getaddr

# Colour classes used for warning messages and important information
# Courtesy of joeld and Peter Mortensen on Stackoverflow
class bcolors:
    WARNING = '\033[91m'
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'

# Aquires the hostname of host then converts name into ipv4 address
hostname = socket.gethostname()
hostaddr = socket.gethostbyname(hostname)

# Server will be bound to internal port 9900
hostport = 9900

# Initial networking information output
print(f"Your public IP address is  -->{bcolors.OKGREEN}{getaddr()}{bcolors.ENDC}<--")
print(f"Your port for this game is -->    {bcolors.OKGREEN}{hostport}{bcolors.ENDC}     <--")
print("Give these two values to the other player joining you\n")

# Mandatory networking warning
print(f"{bcolors.WARNING}WARNING:{bcolors.ENDC} Sharing this address with malicious third parties can open up your entire home network \n to malicious attacks. Ensure you trust the person you are giving it to.")



# Creates a socket object and binds it to the specified ipv4 and port.
# Max incomming request cue is set to 3 due to this being a 1v1 game allowing for a little margin of error. 
# Though UDP could work, TCP is used for the sake of maintaining a continuous connection and making
# packet loss more easily detectable
hostsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsock.bind((hostaddr,hostport))
hostsock.listen(3)

# while loop will run until a connection has been established with player client
print("\nAwaiting connection from client")
while True:
    # Accepts incomming connections and assignes them to object "client" 
    client, address = hostsock.accept()
    # Print success message if client has connected
    if client != None:
        print("Connection with client has been established!")
        break

# Having established a connection between both parties gameplay can now begin
# Gameplay flow:
# game() calls upon necesarry functions and parses all necesarry arguments to
# selectmove(), winner(), and end() respectively
# At every stage of the process the client is instructed to follow suit of flow
# through commands such as "moveselect"

# Winner determination algorithm courtesy of Christopher Shroba on Stackoverflow
# Miles more elegant than a dictionary or 9 if statements

def game():
    while True:
        # Assigned results of selectmove() function to moves variable
        # this is then split up into the host's move and the client's move
        moves = selectmove()
        hostmove = moves[0]
        clientmove = moves[1]
        victor = winner(hostmove, clientmove)
        
        # Client recieves move before print to compensate for voice call lag
        # so as to avoid premptive celebration by host.
        client.send(bytes("victor", "utf-8"))
        client.send(bytes(str(victor), "utf-8"))
        print(victor)
        
        # Call end function to prompt both parties for a redo
        end()

def selectmove():
    client.send(bytes("moveselect","utf-8"))
    while True:
        # Prompt host for move
        hostmove = str(input(f"Please choose your move (Rock, Paper, or Scissors): "))
        recieved = 0

        # If host selects an invalid move, prompt a redo
        if hostmove not in moveset:
            print("You have selected a nonexistent move. Remember the move must be capitalised")
            continue

        # If host selects an appropriate move convert it to the corisponding number (as string),
        # and return host and client move as numbers. Client must convert on their end before
        # transmission to host.
        else:
            hostmove = moveset[hostmove]
            client.send(bytes(str(hostmove),'utf-8'))
            print("Awaiting client move")
            # Await client's move
            clientmove = client.recv(1024)
            clientmove = int(clientmove.decode('utf-8'))
            return((hostmove, clientmove))

def winner(p1, p2):
    if (p1+1) % 3 == p2:
        return "\nClient wins\n"
    elif p1 == p2:
        return "\nIt's a draw\n"
    else:
        return "\nHost wins\n"

def end():
    print("Awaiting client's verdict on rematch")
    # Await client response for a replay
    clientchoice = client.recv(1024)
    clientchoice = clientchoice.decode('utf-8')
    if clientchoice == "y":
        print("The client has requested a rematch")
    # Prompt host for a replay choice
    while True:
        replay = str(input("Would you like to play again? (y/n): "))
        if replay not in ["y","n"]:
            print("You have made an invalid selection. Please try again")
            continue
        else:
            break
    if replay == "y" and clientchoice == "y":
        game()
    else:
        client.send(bytes("noreplay","utf-8"))
        print("One or more parties have declined a rematch")
        print("Thank you for playing! :)")
        client.close()
        exit()


# Players will be prompted for a move as a string for user friendliness
# The moveset dictionary will be used used to convert
moveset = {
        "Rock":int(0),
        "Paper":int(1),
        "Scissors":int(2),
        }

game()


