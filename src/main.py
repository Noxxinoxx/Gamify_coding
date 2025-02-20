import processes

def main():
    """
     Main function handels the startup.
    """    
    process_class = processes.Processes()

    print(f"you had {process_class.runCheck()} bad processes running!")



if __name__ == "__main__":
    main()
