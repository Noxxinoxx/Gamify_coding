#this will be the start.
#we need to read some cool things.
#like games and coding things like terminal.

import wmi
import os
import json

database_file = os.getcwd() + "/Gamify_coding_database.json" 
config_file = os.getcwd() + "/config.json"

def main():

    print("List of all the processes!")
     

    process_win = wmi.WMI()

    config_read = open(config_file)
    
    json_config = json.load(config_read)


    for process in process_win.Win32_Process():
       for bad_processes in json_config[0]["bad_processes"]:
            if(bad_processes == process.Name):
                print("this is a bad process running pls stop that! " + process.Name)




main()
