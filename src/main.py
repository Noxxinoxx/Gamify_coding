import processes
import timer;
import game;
import config
def main():
    """
     Main function handels the startup.
    """    
    
    if config.os == "linux":
        #run a linux version of the code base then!
        #this is just a test atm and we wont add any of the linux code in this commit.
        #but my intension will be to add it shortly!.
        j = 1;

    process_class = processes.Processes()

    print(f"you had {process_class.runCheck()} bad processes running!")
    
    game_timer = timer.Timer(game.Game())

    game_timer.run_program();


if __name__ == "__main__":
    main()
