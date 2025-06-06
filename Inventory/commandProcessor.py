from file_handler import *
from .user import User
from . import Inventory
from colorama import Fore, Style, init
import getpass



def main(user:User , inventory:Inventory , BOLD):
    print(BOLD + Fore.WHITE + "\nCommands of the program\n")
    help_command()
    while True:
        command = input(BOLD + Fore.BLUE + "\nEnter Command :")
        match command:
            case "quit":
                print(BOLD + Fore.GREEN + "GOOD BYE FRIEND")
                return
            case "inventory":
                print(BOLD + Fore.CYAN + "\nInvetory of ABC Traders")
                inventory.display_items()
            case "help":
                print(BOLD + Fore.CYAN + "Commands of the program\n")
                help_command()
            case "change_password":
                print(BOLD + Fore.YELLOW + "PASSWORD CHANGE")
                old_password = getpass.getpass(BOLD + Fore.BLUE + "Enter old password :")
                new_password = getpass.getpass(BOLD + Fore.BLUE + "Enter new password :")
                if user.change_password(old_password , new_password):
                    print(BOLD + Fore.GREEN + "Password was changed successfully")
                else:
                    print(BOLD + Fore.RED + "Password does not match")
            case "delete_account":
                print(BOLD + Fore.YELLOW + "ACCOUNT DELETION")
                password = getpass.getpass(BOLD + Fore.BLUE + "Enter Your password :")
                if user.delete_user(password):
                    print(BOLD + Fore.YELLOW + "Your account has been deleted")
                    return
                else:
                    print(BOLD + Fore.RED + "Account could not be deleted , password may be invalid")
            case "add_item":
                print(BOLD + Fore.CYAN + "ITEM ADDITION")
                try:
                    item_name = input("Enter item name :")
                    quantity = int(input("Enter quantity :"))
                    price = float(input("Enter price :"))
                    if inventory.add_item(item_name , quantity , price):
                        print(BOLD + Fore.YELLOW + item_name + " has beem added to the system")
                    else:
                        print(BOLD + Fore.YELLOW + item_name + " could not be added it may already exist")
                except ValueError:
                    print(BOLD + Fore.RED + "price or quanity is not a valid number or price")
            case "remove_item":
                print(BOLD + Fore.CYAN + "ITEM UPDATE")
                item_name = input(BOLD + Fore.BLUE + "Enter item name :")
                if inventory.remove_item(item_name): 
                    print(BOLD + Fore.YELLOW + item_name + " has been deleted on the system")
                else:
                    print(BOLD + Fore.RED + "Item could not be deleted , it may not exist.")
            case "update_item":
                try:
                    item_name = input("Enter item name :")
                    quantity = int(input("Enter quantity :"))
                    price = float(input("Enter price :"))
                    if inventory.update_item(item_name , quantity , price):
                        print(BOLD + Fore.YELLOW + item_name + " has been updated")
                    else:
                        print(BOLD + Fore.YELLOW + item_name + " could not be updated it may not already exist")
                except ValueError:
                    print(BOLD + Fore.RED + "price or quanity is not a valid number or price")
            case _:
                print(BOLD + Fore.RED + "Invalid Chosen Command")