**About the project**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project is a tcp chat client using tkinter for the gui. This was built off the tcp_server_client repo as it was meant to be a modular backbone for the tcp socket projects I'm building. 

The server is able to keep track of all active connections and mediate a conversation between the connected clients. I need to add a couple of tests to make sure the server is able to remove the correct client socket object from the list of global clients. There is also an error imposed on the server wherein it's thrown into an infinite loop when the client suddenly shuts down. This will be fixed soon.

**Built with**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project was built with python using tkinter. 


**Getting started**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Clone the repo
  `git clone https://github.com/lago77/guichat`

2. Run mainfile.py
  `mainfile.py`

3. On the same machine or another run client.py along with the ip of the machine the server is hosted on
  `frontend.py <host ip>`
