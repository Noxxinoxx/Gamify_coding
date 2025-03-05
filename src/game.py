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


        #need to fix the get data later now we just use the standrad tool


        #this code here where we save the updated thing lp in a class varible might be good if we send alot of things to
        #our database. if we get the steak from a database call then the save mechanics will be redundent.

        

        lp_gain = self.user_database[0]["LP_gain"]
        lp = self.user_lp;
        new_lp = lp + lp_gain;
        self.user_lp = new_lp;
        self.update_streak(True);

        database = tools.read_from_database();

        win_streak = database[0]["win_streak"];
        
        new_lp = new_lp + (win_streak * 2);

        tools.update_value_in_database("LP", new_lp);

        print(f"Good Job you won the game you got {new_lp}")
        
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
        self.update_streak(False);

    def update_streak(self, win):
        """
        updates a users win or lose streak depending on the win varible.
        can also reset a steak
        """
        database = tools.read_from_database();

        if win:
            database[0]["win_streak"] = database[0]["win_streak"] + 1;
            database[0]["lose_streak"] = 0;
        else: 
            database[0]["lose_streak"] = database[0]["lose_streak"] + 1;
            database[0]["win_streak"] = 0;
 

        tools.write_database(database);
    









