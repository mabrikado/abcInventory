from file_handler import *
from .user import User
from . import Inventory
from colorama import Fore, Style, init
import getpass



def main(user:User , inventory:Inventory , BOLD):
    print(BOLD + Fore.WHITE + "\nCommands of the program\n")
    help_command()
    while True:
        command = input(BOLD + Fore.CYAN + "\nEnter Command :")
        match command:
            case "quit":
                return
            case "inventory":
                print(BOLD + Fore.GREEN + "\nInvetory of ABC Traders")
                inventory.display_items()
            case "help":
                help_command()
            case "change_password":
                old_password = getpass.getpass(BOLD + Fore.CYAN + "Enter old password :")
                new_password = getpass.getpass(BOLD + Fore.CYAN + "Enter new password :")
                if user.change_password(old_password , new_password):
                    print(BOLD + Fore.GREEN + "Password was changed successfully")
                else:
                    print(BOLD + Fore.RED + "Password does not match")
            case "delete_account":
                pass
            case "delete_account":
                pass
            case "add_item":
                pass
            case "remove_item":
                pass
            case "update_item":
                pass