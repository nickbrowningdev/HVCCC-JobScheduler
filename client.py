from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time
import menu

# GLOBAL CONSTANTS
SERVER = "10.0.0.121"
PORT = 5050
BUFFSIZE = 2048
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8" 

# GLOBAL VARIABLES

def client_hvccc():
    # creates a client socket
    client_socket = socket(AF_INET, SOCK_STREAM)

    # attaches socket, then connects to server
    client_socket.connect(ADDRESS)

    # verification message
    verf_msg = "HVCCC Job Scheduler"

    # loops until user disconnects
    while True:

        # message sent to the server
        client_socket.send(verf_msg.encode("utf8"))

        # message received from server
        data = client_socket.recv(2048)

        # print the received message
        # it will be reversed
        print("Received from the HVCCC server:", str(data.decode("utf8")))

        # goes to user interface
        menu.display_menu()

        # ask the client whether he wants to continue
        ans = input("\nDo you want to continue(y/n) :")

        if ans == "y":
            continue
        else:
            break
    
    # closes the connection
    client_socket.close()

if __name__ == "__main__": 
    client_hvccc()