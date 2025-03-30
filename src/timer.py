import time;
import config;
import connection;
class Timer:

    def __init__(self, game):
        """
        The init takes a time that is the lenght of the game and a interval that is the interval between games.
        """
        self.length = config.game_length;
        self.interval = config.check_processes_interval;
        self.interval_counter = 0;
        self.current_time = 0;
        self.game = game;
        self.check_interval = config.check_processes_interval;
        self.strikes = config.strikes;
        self.paused = False;
        #inits the api.
        self.api = connection.Connection(self,self.game);

    def run_program(self):
        """
        Starter function to run the program and keep it running until you terminate the program.
        """ 
        self.start_new_game();
        while True:
            #wait for 1 sec between game cycles.
            time.sleep(1);  
            #run the connection to the api.
            
            #try:
            self.api.run_api();
            #except:
            #    print("Error : background api did not init correctly.");

            if self.paused:
                print("game is paused")
            else:
                if(self.game.game_status()):
                    #update timer.
                    print("game is running!")
                    if(self.current_time % self.check_interval == 0):
                        if not self.game.keep_game_running():
                            #then the game is over and we restart.
                            self.start_interval_counter();
                            self.game.game_done(False);                    
                    self.update_time();
                elif(self.game.game_mode == "i"):
                    self.update_interval_counter();
                    print(f"{self.interval - self.interval_counter} sec until next game starts!");
                
                else:
                    print("no games are running!");



    def start_interval_counter(self):
        """
        Used when you want to start the inveral counter between games if you have the intverval game mode on.
        """
        self.interval_counter = 0;
    
    def update_interval_counter(self):
        """
        updates the interval every secound in the game loop.
        """
        self.interval_counter += 1;
        if(self.interval_counter == self.interval):
            self.start_new_game();

    
    def start_new_game(self):
        """
        This function start a new game. it will get all the data from the self functions.
        """
        #start the timer for a new game.
        print("new game has been started hope you win.")
        self.current_time = 0;
        self.game.change_game_status(True);

    def update_time(self):
        """
        updates the current time in the game.
        """
        self.current_time += 1;
        if(self.current_time >= self.length):
            print("games is over well done you made it!");
            self.game.game_done(True);
            self.start_interval_counter();

    def remove_one_strike(self):
        """
        This function will remove a strike from the game.
        """
        self.strikes = self.strikes - 1;

    def validate_strikes(self):
        """
        This function will check your strikes and see if you have any left.
        """
        if(self.strikes > 0):
            return True;
        else: 
            return False;

    def reset_strikes(self):
        """
        This function will reset the strikes to the config standard.
        """
        self.strikes = config.strikes;
    
    def pause_game(self) : 
        """
        This function sets the game to pause.
        """
        if self.validate_strikes(): 
            self.remove_one_strike()
            self.paused = True;
        else:
            print("Game cant be paused anymore you are out of strikes");
        

    def unpause_game(self): 
        """
        This function unpauses the game.
        """
        self.paused = False;






