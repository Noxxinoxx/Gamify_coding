import config
import processes
import tools
class Game:
    def __init__(self):
        self.game_number = 0;
        self.game_mode = config.gameMode;
        self.game_running = False;
        self.user_database = tools.read_from_database();
        self.user_lp = self.user_database[0]["LP"];
    
    def update_game_number(self):
        """
        updates the game number this is part of the game logic for later.
        """
        self.game_number = self.game_number + 1;
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
    def game_check_processes(self):
        """
        This is called when the timer or other process wants to use the game logic for checking the processes running on the system
        """
        p = processes.Processes();
        values = p.runCheck();

        if(values["bad_processes"] >= 1):
            return False

        return True;

    def keep_game_running(self):
        """
        returns if the we keep the game running and no bad processes has been started.
        """
        return self.game_check_processes();
    
    def win(self):
        """
        This function gets called when you win a game.
        """

        lp_gain = self.user_database[0]["LP_gain"]
        lp = self.user_lp;
        new_lp = lp + lp_gain;
        self.user_lp = new_lp;
        tools.update_value_in_database("LP", new_lp);

        print(f"Good Job you won the game you got {lp}")
        
        

        self.update_game_number();
        self.change_game_status(False);


    def game_lost(self):
        """
        This function is called when we lose a game.
        """    
        #here we add points that the user lost.
        print("Game over you lost because you opened a process on the bad list!")
        self.update_game_number();
        self.change_game_status(False);    








