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

    f = wmi.WMI()
        
    config_read = open(config_file)
    
    json_config = json.load(config_read)

   
    for process in f.Win32_Process():
       for bad_processes in json_config[0]["bad_processes"]:
            if(bad_processes == process.Name):
                #this is a process that will run every 10 min or so. 
                #and if it finds that we are running process that we should not then it will add that to a negative queue and remove lp from out account.
                #same gose for the good prcocesses that are running.
                print("this is a bad process running pls stop that! " + process.Name)




main()
