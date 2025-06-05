from typing import Union
from file_handler import *

class User:
    def __init__(self , username:str , password:str , user_handler:UserHandler):
        self.username:str = username
        self.password:str = password
        self.user_handler:UserHandler = user_handler

    @staticmethod
    def create_user(username:str , password:str , user_handler:UserHandler) -> Union["User" , None]:
        if user_handler.write_user(username , password):
            return User(username , password , user_handler)

    def delete_user(self) -> bool:
        return self.user_handler.delete_user(self.username)

    def change_password(self , old_password:str , new_password:str) -> bool:
        if old_password == self.password:
            return self.user_handler.write_user(self.username , new_password , True)
        return False

    @staticmethod
    def log_user(username:str , password:str , user_handler:UserHandler) -> Union["User" , None]:
        #check user exist
        user = user_handler.read_user(username)
        if not user:
            return
        
        if user[1] != password:
            return
        
        return User(username , password , user_handler)
    
    def __eq__(self, value:"User"):
        if not isinstance(value , User):
            return False
        return self.username == value.username and self.password == value.password and self.user_handler == value.user_handler