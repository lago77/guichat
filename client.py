import socket, argparse
from server import Server
from tkinter import *
from threading import Thread
import time

class Client(Server):#inherits from the Server class
    #initializes the client connection to the server on the specified address
    def __init__(self, address,port):
        print("in the client")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address,port))

        
    def return_socket(self):
        return self.sock
    
def send_msg(clientsock,input):
    INPUT = input.get("1.0", "end-1c")
    #print("this is the input " +INPUT)
    INPUT=INPUT+"?"
    input_e=INPUT.encode('ascii')
    clientsock.sendall(input_e)
    #print("sent this "+str(INPUT))
    
    
def outputting(myclient,sc,output):
    #print("in the output")
    while True:
        newmsg = myclient.recv_msg(sc,b'?')
        newmsge=newmsg.decode('ascii')
        output.insert(END,(newmsge))

    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")
    parser.add_argument("--port", default=1060)
    args = parser.parse_args()

    ###Produces the main window to place gui widgets on
    root = Tk()
    root.geometry("300x250")
    root.title(" Welcome to the chat screen ")



    ###Produces a new client object and returns its socket object
    newclient = Client(args.ip,args.port)
    clientsock = newclient.return_socket()
    newsock=newclient.return_socket()



    print("the type is "+str(type(newsock)))

    #creates the gui widgets. Chatinput that feeds messages/data to the server, chatOutput that receives data from the server/other clients and #Display for the send chat button.
    chatInput = Text(root, height = 5,
				width =30,
				bg = "thistle2")

    chatOutput = Text(root, height = 12,
                width = 100,
                bg = "snow4")

    Display = Button(root, height = 5,
                    width = 10,
                    text ="Send",
                    bg="thistle4",
                    command = lambda:send_msg(newsock,chatInput))

    ###places and positions the created widgets in their listed order.
    chatOutput.pack()
    chatInput.pack()
    chatInput.place(x=2, y=190)
    Display.pack()
    Display.place(x=220,y=190)
    
    ###created a tuple argument to be fed into the thread target
    t=(newclient,newsock,chatOutput)

    Thread(target=outputting,args=t).start()
  
    mainloop()

