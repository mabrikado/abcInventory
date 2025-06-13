from typing import Union
from file_handler import *
from databaseSQL import DatabaseSQL


class UserException(Exception):
    pass

class User:
    """
    Represents a user with authentication capabilities via UserHandler.

    Attributes:
        username (str): The username of the user.
        password (str): The user's password stored as a string.
        user_handler (UserHandler): The handler to read/write user data.
    """

    def __init__(self, username: str, password: str, user_handler: UserHandler = None , database:DatabaseSQL=None):
        """
        Initialize a User instance.

        Args:
            username (str): The user's username.
            password (str): The user's password (plain text).
            user_handler (UserHandler): The user data handler instance.
        """
        self.username: str = username
        self.password: str = password
        self.user_handler: UserHandler = user_handler
        self.database:DatabaseSQL = database

        if not database and not user_handler:
            raise UserException("User has no data to read")

    @staticmethod
    def create_user(username: str, password: str, user_handler: UserHandler) -> Union["User", None]:
        """
        Create a new user with hashed password and write it to file using user_handler.

        Args:
            username (str): The desired username.
            password (str): The user's plain text password.
            user_handler (UserHandler): Handler to persist user data.

        Returns:
            User | None: Returns the User object if creation was successful, None otherwise.
        """
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")  # store as str, not bytes
        if user_handler.write_user(username, password_hash):
            return User(username, password, user_handler)
        return None

    def delete_user(self, password: str) -> bool:
        """
        Delete the user if the provided password matches the current password.

        Args:
            password (str): Password to verify deletion.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if password != self.password:
            return False
        return self.user_handler.delete_user(self.username)

    def change_password(self, old_password: str, new_password: str) -> bool:
        """
        Change the user's password if the old password matches.

        Args:
            old_password (str): The current password.
            new_password (str): The new password to set.

        Returns:
            bool: True if password was changed, False otherwise.
        """
        if old_password == self.password:
            hashed_new = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
            self.user_handler.write_user(self.username, hashed_new, True)
            self.password = new_password
            return True
        return False

    @staticmethod
    def log_user(username: str, password: str, user_handler: UserHandler) -> Union["User", None]:
        """
        Authenticate a user by username and password.

        Args:
            username (str): The username to log in.
            password (str): The password provided for authentication.
            user_handler (UserHandler): Handler to read user data.

        Returns:
            User | None: Returns a User object if authentication succeeds, else None.
        """
        user = user_handler.read_user(username)
        if not user:
            return None
        if not bcrypt.checkpw(password.encode("utf-8"), user[1].encode('utf-8')):
            return None
        return User(username, password, user_handler)

    def __eq__(self, value: "User") -> bool:
        """
        Equality check between two User objects.

        Args:
            value (User): Another user instance.

        Returns:
            bool: True if username, password, and user_handler are equal, False otherwise.
        """
        if not isinstance(value, User):
            return False
        return (self.username == value.username and 
                self.password == value.password and 
                self.user_handler == value.user_handler)

    def __str__(self) -> str:
        """
        String representation of the User.

        Returns:
            str: The username.
        """
        return f"{self.username}"
