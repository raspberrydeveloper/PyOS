import colorama as c
import platform

c.init(autoreset=True)

username = ""

def shell(username):
    command = input(c.Fore.RED + f"{username}" + c.Fore.BLUE +
                    "@" + c.Fore.GREEN + "pyos: " + c.Fore.LIGHTBLACK_EX)
    if command != "":
        try:
            program, params = command.split(" ", 1)
        except ValueError:
            params = ""
            program = command
        try:
            program = __import__(
                f"System.programs.{program}", fromlist=['run'])
            program.run(params, username)
        except ModuleNotFoundError:
            print(c.Fore.RED + "Command " + c.Fore.YELLOW +
                  program + c.Fore.RED + " not found!")


def set_shell_username(new_username):
    global username
    username = new_username

def shell_manager():
    global username
    while True:
        shell(username)
