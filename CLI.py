import Inventory
import getpass
from Inventory import *
from file_handler import *
from tabulate import tabulate
from user import *
from colorama import Fore, Style, init
from commands import *

def main():
    BOLD = '\033[1m'
    print(BOLD + Fore.YELLOW + "ABC TRADERS pty(ltd)\n")
    user_handler = UserHandler("database/Users.txt")
    inventory_handler = InventoryHandler("database/Inventory.txt")
    registrationKey = registration_key("database/registrationKey.txt")
    inventory = Inventory(inventory_handler)
    init()
    
    # #prompt user for choice
    chosen_command = input(Fore.CYAN + BOLD + "Register or Log in (R/L) :").lower()

    # #verify user choice
    if chosen_command  not in ["r" , "l"]:
        print(BOLD + Fore.RED + "Invalid Choice")
        return
    
    print("\n" + BOLD + Fore.GREEN + ("ACCOUNT REGISTRATION" if chosen_command == "r" else "LOGIN") + "\n")

    user_input  = input(BOLD + Fore.CYAN + "Enter username :")
    password_input = getpass.getpass(BOLD + "Enter your password: ")

    user = None

    #log user in
    if chosen_command  == "l":
        user = User.log_user(user_input , password_input , user_handler)
        if not user:
            print(BOLD + Fore.RED +"Username or password is invalid!!")
            return
        command_runner = Command(user , inventory)
        #run commands
        command_runner.run_commands()
    else:

        #get registration
        entered_Key = input(BOLD + Fore.YELLOW + "Enter registration key :")

        #validate key
        if entered_Key != registrationKey:
            print(BOLD + Fore.RED + "Invalid Registration Key")
            return

        #register a user
        user = User.create_user(user_input , password_input , user_handler)
        if user:
            print(BOLD + Fore.GREEN + "User registered successfully")
            command_runner = Command(user , inventory)
            #run commands
            command_runner.run_commands()
        else:
            print(BOLD + Fore.RED + "Something went wrong , User may already exist")
            


if __name__ == "__main__":
    main()