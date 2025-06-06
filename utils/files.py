from typing import List
from tabulate import tabulate
from colorama import Fore, Style, init
BOLD = '\033[1m'


def registration_key(filepath:str)->str:
    with open(filepath , "r") as file:
        return file.read()

def readlines(path , strip=False) -> List[str]:
    with open(path , "r") as file:
        lines = file.readlines()
        newLines = []
        for line in lines:
            if line == "\n":
                continue
            if strip:
                newLines.append(line.strip())
            else:
                newLines.append(line)    
        return newLines


def clean_txt_data(path):
    users =readlines(path , True)
    with open(path , 'w') as file:
        file.writelines(list(map(lambda a : a + "\n" , users)))

def help_command():
    init()
    headers = [BOLD + "COMMAND" ,BOLD + "DETAILS"]
    data = [["help" , "display info about other commands"] , 
            ["add_item" , "Add item to inventory"] , 
            ["remove_item" , "Delete Item in Inventory"] , 
            ["update_item" , "Update information about item"],
            ["inventory" , "Display a table of inventory"] ,
            ["change_password" , "Change your password to new password"] , 
            ["delete_account" , "delete your account"] , 
            ["quit" , "Exit Program"]]
    print(Fore.CYAN + tabulate(data , headers , tablefmt="grid"))