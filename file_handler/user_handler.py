from typing import *
from . import utils

class UserHandler:
    def __init__(self , path):
        self.path = path

    def write_user(self, username, password, override=False):
        user = self.read_user(username)
        if user and not override:
            return False

        user_deleted = None
        if override:
            user_deleted = self.delete_user(username)

        with open(self.path, "a") as file:
            file.write(f"{username} {password}\n")    



        return True

    def read_user(self , username) -> List[str]:
        with open(self.path , "r") as file:
            users = file.readlines()
            for line in users:
                if username in line:
                    return line.replace("\n" , "").split(" ")
                
    def delete_user(self, username):

        user = self.read_user(username)

        if not user:
            return False

        def exclude_user(user):
            return not user.startswith(username + " ")  # could use stricter matching if needed

        users = utils.readlines(self.path)  # read first, before wiping the file

        with open(self.path, "w") as file:
            file.writelines(filter(exclude_user, users))
        
        #clean data
        utils.clean_txt_data(self.path)
        return True

    def is_file_empty(self):
        try:
            with open(self.path , "r") as file:
                if len(file.read()) == 0:
                    return True
                return True
        except FileNotFoundError:
            return True    

# filehandler = UserHandler("users.txt")
# filehandler.write_user("sibusiso" , "abc#")

# # filehandler.write_user("mabrikado" , "assd#" , True)
# # print(filehandler.read_user("sibusiso"))
# # print(utils.readlines(filehandler.path))
# filehandler.delete_user("efg")
# filehandler.delete_user("sibusiso")
# print(utils.readlines(filehandler.path , True))


