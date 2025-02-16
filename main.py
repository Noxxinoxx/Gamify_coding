#this will be the start.
#we need to read some cool things.
#like games and coding things like terminal.

import wmi


def main():

    print("List of all the processes!")

    f = wmi.WMI()

    for process in f.Win32_Process():
        print(f"{process.ProcessId:<10} {process.Name}")
    

main()
