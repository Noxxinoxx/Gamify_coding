import threading;

class Thread_handler:
    def __init__(self): 
        self.command_queue = [];
        self.responde_queue = [];
        self.thread_list = [];

    def create_thread(self, target_function):
        """
        This will create a thread.
        """
        x = threading.Thread(target=target_function);
        self.thread_list.append(x);
        return x;
    
    def add_to_command_queue(self, data):
        """
        Adds a new command to the command queue the gamelogic api will handle the command after
        wards and send it back in responde queue;
        """
        assert isinstance(data, str) == True;
        self.command_queue.append(data)

    def add_to_responde_queue(self, data):
        """
        Adds a new responde to responde queue;
        """
        assert isinstance(data, str) == True;
        self.responde_queue.append(data);
