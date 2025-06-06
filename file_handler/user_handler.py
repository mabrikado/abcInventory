from typing import *
from ..utils import files
import bcrypt

class UserHandler:
    def __init__(self , path):
        self.path = path

    def write_user(self, username, password, override=False) -> bool:
        user = self.read_user(username)
        if user and not override:
            return False
        if override:
            self.delete_user(username)
        with open(self.path, "a") as file:
            file.write(f"{username} {password}\n")    
        return True

    def read_user(self , username) -> List[str]:
        with open(self.path , "r") as file:
            users = file.readlines()
            for line in users:
                if username in line:
                    return line.replace("\n" , "").split(" ")
                
    def delete_user(self, username) -> bool:

        user = self.read_user(username)

        if not user:
            return False

        def exclude_user(user):
            return not user.startswith(username + " ") 

        users = files.readlines(self.path) 

        with open(self.path, "w") as file:
            file.writelines(filter(exclude_user, users))
        
        #clean data
        files.clean_txt_data(self.path)
        return True

    def is_file_empty(self) -> True:
        try:
            with open(self.path , "r") as file:
                if len(file.read()) == 0:
                    return True
                return True
        except FileNotFoundError:
            return True


