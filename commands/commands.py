from Inventory import *
import getpass
from user import *
BOLD = '\033[1m'

class CommandException(Exception):
    """Exception raised for invalid commands in Command processor."""
    pass

class Command:
    """
    Command processor class to handle user commands related to user management 
    and inventory operations.

    Attributes:
        user (User): The current logged-in user.
        inventory (Inventory): The inventory instance to manipulate.
    """

    def __init__(self, user: User, inventory: Inventory):
        """
        Initialize Command processor with user and inventory instances.

        Args:
            user (User): Current logged-in user object.
            inventory (Inventory): Inventory instance for item operations.
        """
        self.user = user
        self.inventory = inventory
    
    def processor(self, command: str):
        """
        Process a given command string and perform associated action.

        Args:
            command (str): The command string input by the user.

        Raises:
            CommandException: If the command is not recognized.
        """
        if command.lower() not in ["quit", "change_password", "delete_account", 
                                   "add_item", "remove_item", "update_item", 
                                   "inventory", "help"]:
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
        """
        Prompt user to change their password, verifying old password and 
        setting a new one.
        """
        print(BOLD + Fore.YELLOW + "PASSWORD CHANGE")
        old_password = getpass.getpass(BOLD + Fore.BLUE + "Enter old password :")
        new_password = getpass.getpass(BOLD + Fore.BLUE + "Enter new password :")
        if self.user.change_password(old_password, new_password):
            print(BOLD + Fore.GREEN + "Password was changed successfully")
        else:
            print(BOLD + Fore.RED + "Password does not match")
    
    def delete_account(self):
        """
        Prompt user for password and attempt to delete their account.
        """
        print(BOLD + Fore.YELLOW + "ACCOUNT DELETION")
        password = getpass.getpass(BOLD + Fore.BLUE + "Enter Your password :")
        if self.user.delete_user(password):
            print(BOLD + Fore.YELLOW + "Your account has been deleted")
            return
        else:
            print(BOLD + Fore.RED + "Account could not be deleted, password may be invalid")
    
    def add_item(self):
        """
        Prompt user to input details for a new inventory item and add it.
        """
        print(BOLD + Fore.CYAN + "ITEM ADDITION")
        try:
            item_name = input(BOLD + Fore.BLUE + "Enter item name :")
            quantity = int(input(BOLD + Fore.BLUE + "Enter quantity :"))
            price = float(input(BOLD + Fore.BLUE + "Enter price :"))
            if self.inventory.add_item(item_name, quantity, price):
                print(BOLD + Fore.YELLOW + item_name + " has been added to the system")
            else:
                print(BOLD + Fore.YELLOW + item_name + " could not be added; it may already exist")
        except ValueError:
            print(BOLD + Fore.RED + "Price or quantity is not a valid number")
    
    def remove_item(self):
        """
        Prompt user to input an item name and remove it from inventory.
        """
        print(BOLD + Fore.YELLOW + "ITEM DELETE")
        item_name = input(BOLD + Fore.BLUE + "Enter item name :")
        if self.inventory.remove_item(item_name): 
            print(BOLD + Fore.YELLOW + item_name + " has been deleted from the system")
        else:
            print(BOLD + Fore.RED + "Item could not be deleted; it may not exist.")
    
    def update_item(self):
        """
        Prompt user to input item details and update the existing item.
        """
        try:
            item_name = input(BOLD + Fore.BLUE + "Enter item name :")
            quantity = int(input(BOLD + Fore.BLUE + "Enter quantity :"))
            price = float(input(BOLD + Fore.BLUE + "Enter price :"))
            if self.inventory.update_item(item_name, quantity, price):
                print(BOLD + Fore.YELLOW + item_name + " has been updated")
            else:
                print(BOLD + Fore.YELLOW + item_name + " could not be updated; it may not already exist")
        except ValueError:
            print(BOLD + Fore.RED + "Price or quantity is not a valid number")
    
    def run_commands(self):
        """
        Display available commands and start a loop to process user commands 
        until quit is issued.
        """
        print(BOLD + Fore.GREEN + "\nCommands of the program\n")
        help_command()
        while True:
            command = input(BOLD + Fore.BLUE + "Enter Command :")
            try:
                self.processor(command)
            except CommandException as e:
                print(BOLD + Fore.RED + str(e))

