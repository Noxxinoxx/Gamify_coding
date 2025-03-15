import processes
import timer;
import game;

def main():
    """
     Main function handels the startup.
    """ 
    
    game_timer = timer.Timer(game.Game())

    game_timer.run_program();


if __name__ == "__main__":
    main()
