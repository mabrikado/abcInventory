from typing import *
from utils import files
import bcrypt

class UserHandler:
    """
    A handler class to manage user data such as writing, reading, deleting users
    from a text file-based storage.
    """

    def __init__(self, path):
        """
        Initialize the UserHandler with a given file path.

        Args:
            path (str): Path to the file where user data is stored.
        """
        self.path = path

    def write_user(self, username, password, override=False) -> bool:
        """
        Write a new user or update an existing one.

        Args:
            username (str): The username to write.
            password (str): The hashed password.
            override (bool): If True, overrides the existing user.

        Returns:
            bool: True if the user was written successfully, False otherwise.
        """
        user = self.read_user(username)
        if user and not override:
            return False
        if override:
            self.delete_user(username)
        with open(self.path, "a") as file:
            file.write(f"{username} {password}\n")    
        return True

    def read_user(self, username) -> List[str]:
        """
        Read a user's data by username.

        Args:
            username (str): The username to find.

        Returns:
            List[str]: A list containing the username and password, or None if not found.
        """
        with open(self.path , "r") as file:
            users = file.readlines()
            for line in users:
                if username in line:
                    return line.replace("\n" , "").split(" ")

    def delete_user(self, username) -> bool:
        """
        Delete a user from the storage file.

        Args:
            username (str): The username to delete.

        Returns:
            bool: True if the user was deleted, False otherwise.
        """
        user = self.read_user(username)

        if not user:
            return False

        def exclude_user(user:str):
            return not user.startswith(username + " ") 

        users = files.readlines(self.path) 

        with open(self.path, "w") as file:
            file.writelines(filter(exclude_user, users))
        
        #clean data
        files.clean_txt_data(self.path)
        return True

    def is_file_empty(self) -> True:
        """
        Check if the user file is empty.

        Returns:
            True: Always returns True if the file is empty. 
            If the file does not exist, an exception will be raised unless handled elsewhere.
        """
        with open(self.path , "r") as file:
            return len(file.read()) == 0

