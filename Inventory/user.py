from typing import Union

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password

    @staticmethod
    def create_user(username:str , password:str) -> Union["User" , None]:
        pass

    def delete_user():
        pass

    def change_password(old_password:str , new_password:str) -> str:
        pass

    @staticmethod
    def log_user(username:str , password:str) -> Union["User" , None]:
        pass