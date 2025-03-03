
import wmi
import config
class Processes :
    def __init__(self):
        self.good_processes = config.goodProcesses;
        self.bad_processes = config.badProcesses;
        self.process = wmi.WMI();

    def runCheck(self):
        """
        Runs the check that looks for bad proceses it counts them and the returns the restult.
        """
        bad_processes_running = 0;
        good_processes_running = 0;
        
        for process in self.process.Win32_Process():
            for bad_processes in self.bad_processes:
                if(bad_processes == process.Name):
                    bad_processes_running +=1
            for good_processes in self.good_processes:
                if(good_processes == process.Name):
                    good_processes_running +=1
        return dict(bad_processes = bad_processes_running, good_processes = good_processes_running)

