from Inventory import *
import getpass
BOLD = '\033[1m'

class Command:
    def __init__(self , user:User , inventory:Inventory):
        self.user = user
        self.inventory = inventory
    
    def processor(self , command:str):
        if command.lower() not in ["quit" , "change_password" , "delete_account" , "add_item" , "remove_item" , "update_item" , "inventory" , "help"]:
            raise CommandException(command + " is an Invalid Command")
        
        match command:
            case "quit":
                print(BOLD + Fore.GREEN + "Good Bye Friend")
                quit()
            case "change_password":
                self.change_password()
            case "delete_account":
                self.delete_account()
            case "add_item":
                self.add_item()
            case "remove_item":
                self.remove_item()
            case "update_item":
                self.update_item()
            case "inventory":
                self.inventory.display_items()
            case "help":
                help_command()
    
    def change_password(self):
        print(BOLD + Fore.YELLOW + "PASSWORD CHANGE")
        old_password = getpass.getpass(BOLD + Fore.BLUE + "Enter old password :")
        new_password = getpass.getpass(BOLD + Fore.BLUE + "Enter new password :")
        if self.user.change_password(old_password , new_password):
            print(BOLD + Fore.GREEN + "Password was changed successfully")
        else:
            print(BOLD + Fore.RED + "Password does not match")
    
    def delete_account(self):
        print(BOLD + Fore.YELLOW + "ACCOUNT DELETION")
        password = getpass.getpass(BOLD + Fore.BLUE + "Enter Your password :")
        if self.user.delete_user(password):
            print(BOLD + Fore.YELLOW + "Your account has been deleted")
            return
        else:
            print(BOLD + Fore.RED + "Account could not be deleted , password may be invalid")
    
    def add_item(self):
        print(BOLD + Fore.CYAN + "ITEM ADDITION")
        try:
            item_name = input(BOLD + Fore.BLUE + "Enter item name :")
            quantity = int(input(BOLD + Fore.BLUE + "Enter quantity :"))
            price = float(input(BOLD + Fore.BLUE + "Enter price :"))
            if self.inventory.add_item(item_name , quantity , price):
                print(BOLD + Fore.YELLOW + item_name + " has beem added to the system")
            else:
                print(BOLD + Fore.YELLOW + item_name + " could not be added it may already exist")
        except ValueError:
                print(BOLD + Fore.RED + "price or quanity is not a valid number or price")
    
    def remove_item(self):
        print(BOLD + Fore.YELLOW + "ITEM DELETE")
        item_name = input(BOLD + Fore.BLUE + "Enter item name :")
        if self.inventory.remove_item(item_name): 
            print(BOLD + Fore.YELLOW + item_name + " has been deleted on the system")
        else:
            print(BOLD + Fore.RED + "Item could not be deleted , it may not exist.")
    
    def update_item(self):
        try:
            item_name = input(BOLD + Fore.BLUE + "Enter item name :")
            quantity = int(input(BOLD + Fore.BLUE + "Enter quantity :"))
            price = float(input(BOLD + Fore.BLUE + "Enter price :"))
            if self.inventory.update_item(item_name , quantity , price):
                print(BOLD + Fore.YELLOW + item_name + " has been updated")
            else:
                print(BOLD + Fore.YELLOW + item_name + " could not be updated it may not already exist")
        except ValueError:
                print(BOLD + Fore.RED + "price or quanity is not a valid number or price")
    
    def run_commands(self):
        print(BOLD + Fore.GREEN + "\nCommands of the program\n")
        help_command()
        while True:
            command = input(BOLD + Fore.BLUE + "Enter Command :")
            try:
                self.processor(command)
            except CommandException as e:
                print(BOLD + Fore.RED + str(e))

class CommandException(Exception):
    pass
