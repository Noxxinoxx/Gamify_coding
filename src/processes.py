import config
class Processes :
    def __init__(self):
        self.good_processes = config.goodProcesses;
        self.bad_processes = config.badProcesses;


    def runCheck(self):
        """
        Runs the check that looks for bad proceses on windows and returns the result.
        """
        bad_processes_running = 0;
        good_processes_running = 0;
        

        if config.OS == "Windows":
            import wmi
            proc = wmi.WMI()
            for process in proc.Win32_Process():
                for bad_processes in self.bad_processes:
                    if(bad_processes == process.Name):
                        bad_processes_running +=1
                for good_processes in self.good_processes:
                    if(good_processes == process.Name):
                        good_processes_running +=1

        elif config.OS == "Linux":
            import psutil
            for proc in psutil.process_iter(): 
                for bad_processes in self.bad_processes: 
                    if(bad_processes == proc.name()): 
                        bad_processes_running +=1; 
                for good_processes in self.good_processes: 
                    if(good_processes == proc.name()): 
                        good_processes_running +=1;


        return dict(bad_processes = bad_processes_running, good_processes = good_processes_running)

