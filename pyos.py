#!/usr/bin/python3

from System.core import shell
from System.auth import login
import colorama as c
import time
import threading

c.init(autoreset=True)

# Check that you are running the code directly

if __name__ == "__main__":

    # Wait for user to login
    print(c.Fore.BLUE + "Welcome, please login!" + c.Fore.LIGHTBLACK_EX)
    login_status = login.login_screen()
    tries = 0
    while list([login_status])[0] == False:
        tries += 1
        if tries <= 3:
            print(c.Fore.RED + "Invalid username or password! Please try again." +
                  c.Fore.LIGHTBLACK_EX)
            login_status = login.login_screen()
        else:
            print(c.Fore.YELLOW + "Warning! Maximum tries reached, sleeping 5 seconds bec.fore retrying!" + c.Fore.LIGHTBLACK_EX)
            time.sleep(5)

    # Activate the shell and tell it what username to use
    shell.set_shell_username(login_status[1])
    shell_thread = threading.Thread(target=shell.shell_manager, args=())
    shell_thread.start()
