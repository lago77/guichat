from server import Server
from client import Client
from threading import Thread
import socket

def start_sc_connections(listener, sc):
    t=(listener,)
    newsock=sc
    for i in range(3):
        Thread(target=newsock.serve, args=t).start()


if __name__ == '__main__':
    newserver = Server(socket.gethostbyname(socket.gethostname()),1060)
    listening = newserver.ret_listener()
    
    start_sc_connections(listening,newserver)