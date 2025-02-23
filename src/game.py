
class Game:
    def __init__(self):
        self.game_number = 0;
        self.game_mode = "r";
    
    def update_game_number(self,number):
        """
        updates the game number this is part of the game logic for later.
        """
        self.game_number = number;

