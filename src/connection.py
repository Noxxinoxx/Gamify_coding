import socket
import config
import api

class Connection:
    def __init__(self, game_class):
        """
        inits all the needed things to run the socket. 
        This is the backend code that front end progams uses to talk.
        """
        self.router = api.Router(game_class) 
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
        data = self.conn.recv(512);

        if data:
            respond_data = self.router.router(data);
            print(respond_data)
            return self.send_data(respond_data);
        else:
            print("waiting for data!");
            return None;
    
    def send_data(self, data):
        """
        This function is used to send data from the server to the client.
        """
        self.conn.sendall(data.encode("utf-8"));


