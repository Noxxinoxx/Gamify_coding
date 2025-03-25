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
        self.host = config.host;
        self.addr = None;
        self.conn = None;
        
        self.socket.bind((self.host, self.port));

        self.socket.listen(5);
        
        self.conn, self.addr = self.socket.accept();

    def run_api(self): 
        """
        this function runs every tick the application is running its job is to
        retrive data from a client aka frontend function.
        """    
        #get 1024 bit worth of data;
        data = self.conn.recv(1024);

        if data:
            return self.send_data(data);
        else:
            print("waiting for data!");
            return None;
    
    def send_data(self, data):
        """
        This function is used to send data from the server to the client.
        """
        self.conn.sendall(data);


