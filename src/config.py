import os

paths = dict(
    database_url = os.path.join(os.getcwd(), "../res/Gamify_coding_database.json"),  
)
game_length = 10;
check_processes_interval = 10;
gameMode = "i"
OS = "Linux"
strikes = 2;
port = 3000;


badProcesses = ["cs2.exe", "LeagueClient.exe"]
goodProcesses = ["nvim.exe", "terminal.exe"]    
