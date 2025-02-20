import psutil

# Define sets of good and bad processes
good_processes = {"code", "vscode", "neovim", "terminal", "python"}
bad_processes = {"cs2", "steam", "discord", "chrome"}


def list_running_processes():
    """
    Lists running processes and categorizes them as good, bad, or neutral.
    """
    running_good = []
    running_bad = []
    running_neutral = []

    # Iterate through running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            name = process.info['name'].lower()
            if name in good_processes:
                running_good.append(name)
            elif name in bad_processes:
                running_bad.append(name)
            else:
                running_neutral.append(name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # Print categorized process lists
    print("Good processes running:", ", ".join(running_good) if running_good else "None")
    print("Bad processes running:", ", ".join(running_bad) if running_bad else "None")
    print("Neutral processes running:", ", ".join(running_neutral) if running_neutral else "None")


if __name__ == "__main__":
    list_running_processes()