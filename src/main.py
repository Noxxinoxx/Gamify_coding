import processes
import timer;
import game;

def main():
    """
     Main function handels the startup.
    """    
    process_class = processes.Processes()

    print(f"you had {process_class.runCheck()} bad processes running!")
    
    game_timer = timer.Timer(game.Game())

    game_timer.run_program();


if __name__ == "__main__":
    main()
