
class Game:
    def __init__(self):
        self.game_number = 0;
        self.game_mode = "i";
        self.game_running = False; 
    
    def update_game_number(self,number):
        """
        updates the game number this is part of the game logic for later.
        """
        self.game_number = number;
    def game_status(self):
        """
        gets the game status if we have a running game or not.
        """
        return self.game_running;
    def change_game_status(self, running):
        """
        change the status of the running game used to either start a game or to stop a game.
        change be used if a bad process is lanched to force quit the running game.
        """
        self.game_running = running;
        
