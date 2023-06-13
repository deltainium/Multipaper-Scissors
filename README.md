# Multipaper-Scissors

**The ultimate way to settle any argument.**  
Multipaper-scissors is a CLI-Based multiplayer rock paper scissors game.


## Installation

Unfortunately Linux is currently the only operating system supported.  

To install Multipaper-scissors either download the latest host or client executable from the [releases page](https://github.com/deltainium/Multipaper-Scissors/releases) if you will be hosting or joining a game respectively.  

Then open up your terminal of choice, navigate to the download directory of the file and add execution permissions with:

```bash
sudo chmod +x client
# or
sudo chmod +x host
```
Then run the file with:

```bash
./client
# or
./host
```
 Good luck, have fun!   
## Usage - WAN / Public Internet
**Host:**  
Multipaper-Scissors works by creating a socket on the host's device, and connecting the client to the host's socket via TCP. In practical terms this means that 99%  of the time the host will have to open a TCP port on their home router which forwards all connections to port 9900 on their  local machine. Please refer to your router's manual for more information on port forwarding.  

After succesfully seting up port forwarding simply provide the client user with your public IP and the port used for port forwarding. Upon startup the host executable will print your public IP for your convenience. Please note the client will require your **external port**, i.e the one you you chose when port forwarding. This is **different** from port 9900 which the game uses to talk with your router.  

**Client:**  
Simply enter your host's public IP and external port in the appropriate fields and enjoy the game!

## Usage - LAN / Same router connection
**Host:**  
Provide your client with your local IPv4 address and await a connection.

**Client:**  
Input your host's local IP address and port 9900 as this port is used for all local network communication.
