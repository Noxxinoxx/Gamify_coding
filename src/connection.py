import socket
import config

class Connection:
    def __init__(self):
        """
        inits all the needed things to run the socket. 
        This is the backend code that front end progams uses to talk.
        """
        self.socket = socket.socket();
        self.port = config.port;
        
    def start(self): 
        """
        Use this function to start/init the socket server.
        """

        self.socket.bind(("", self.port));

        self.socket.listen(5);






