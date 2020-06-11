import socket 
from _thread import *
import threading
import time

# GLOBAL CONSTANTS
SERVER = "0.0.0.0"
PORT = 5050
BUFFSIZE = 2048
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# GLOBAL VARIABLES
# creates server socket
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this right here binds the ip address and port number
SERVER.bind(ADDRESS)

# lock
hvccc_lock = threading.Lock()

# thread function
def threaded(client):
    while True: 

        # data received from client
        data = client.recv(2048)
        if not data:
            print("Disconnect")

            # lock released on exit 
            hvccc_lock.release() 
            break
        
        # reverse the given string from client 
        data = data[::-1] 
  
        # send back reversed string to client 
        client.send(data) 
    
    # connection closed
    client.close()


# puts server socket into listening mode
def listen_to_server():
    # puts the socket into listening mode
    SERVER.listen(999)

    # displays that server is waiting for connections
    print("[SERVER] WAITING FOR CONNECTIONS")

    # will loop forever until client wants to exit
    while True:
        # establish connection with client 
        client, addr = SERVER.accept()

        # lock acquired by client
        hvccc_lock.acquire()
        print("[CONNECTION] :", addr[0], ":", addr[1])
        print(f"[CONNECTION] : {time.time()}")

        # start a new thread and return its identifer
        start_new_thread(threaded, (client,)) 

    SERVER.close()

if __name__ == "__main__": 
    # checks if server can be created
    try:
        listen_to_server()
        
    except Exception as ex:
        # error message if server fails to launch
        print(ex)