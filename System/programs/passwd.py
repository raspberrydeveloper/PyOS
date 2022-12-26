from System.auth import password_hasher, database_checker
import sqlite3
import colorama
from colorama import Fore

colorama.init(autoreset=True)

db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def passwd(username, currentusername):
    if currentusername == username:
        if database_checker.check_username(username) == True:
            print(Fore.BLUE + f"Changing password for {username}." + Fore.BLACK)
            if database_checker.check_password(username, password_hasher.hash(input("Current password: "))) == True:
                new_passwd = password_hasher.hash(input("New password: "))
                verify = password_hasher.hash(input("Retype new password: "))
                if new_passwd == verify:
                    cursor.execute(f"update users set password = '{new_passwd}' where username = '{username}'")
                    db.commit()
                    print(Fore.GREEN + "passwd: password updated successfully" + Fore.BLACK)
            else:
                print("passwd: Authentication token manipulation error \npasswd: password unchanged")
        else:
            print(f"passwd: user '{username}' does not exist")
    elif currentusername == "root":
        if database_checker.check_username(username) == True:
            new_passwd = password_hasher.hash(input("New password: "))
            verify = password_hasher.hash(input("Retype new password: "))
            if new_passwd == verify:
                cursor.execute(f"update users set password = '{new_passwd}' where username = '{username}'")
                db.commit()
                print(Fore.GREEN + "passwd: password updated successfully" + Fore.BLACK)
            else:
                print("passwd: Authentication token manipulation error \npasswd: password unchanged")
        else:
            print(f"passwd: user '{username}' does not exist")       
    else:
        print(Fore.RED + f"Only root and {username} can change password!" + Fore.BLACK)
