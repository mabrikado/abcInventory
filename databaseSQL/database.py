from typing import List, Optional, Union
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Base class for models
class Base(DeclarativeBase):
    """Base class for all database models using SQLAlchemy's DeclarativeBase."""
    pass


class User(Base):  
    """
    Represents a user in the system.

    Attributes:
        id (int): Primary key identifier.
        username (str): Unique username.
        password (str): Hashed password.
    """
    __tablename__ = 'users'  
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    def __str__(self):
        """Returns a string representation of the user."""
        return f"{self.username} {self.password}"
    
    def __repr__(self):
        """Returns an unambiguous string representation of the user."""
        return f"{self.username} {self.password}"
    
    def __eq__(self, value):
        """
        Checks equality between two User instances.

        Args:
            value (User): Another user instance.

        Returns:
            bool: True if usernames and passwords match, else False.
        """
        if isinstance(value, User):
            return value.username == self.username and value.password == self.password
        return False


class Item(Base): 
    """
    Represents an item in the inventory.

    Attributes:
        id (int): Primary key identifier.
        name (str): Name of the item.
        quantity (int): Quantity in stock.
        price (float): Price of the item.
    """
    __tablename__ = 'items'  
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    quantity: Mapped[int]
    price: Mapped[int]

    def __eq__(self, value):
        """
        Checks equality between two Item instances.

        Args:
            value (Item): Another item instance.

        Returns:
            bool: True if name, quantity, and price match, else False.
        """
        if isinstance(value, Item):
            return (value.name == self.name and 
                    value.price == self.price and 
                    value.quantity == self.quantity)
        return False

    def __str__(self):
        """Returns a string representation of the item."""
        return f"{self.name} {self.quantity} {self.price}"


class DatabaseSQL:
    """
    Handles database operations for users and items using SQLAlchemy ORM.

    Args:
        url (str): Database connection URL.
    """

    def __init__(self, url):
        self.url = url
        self.engine = create_engine(self.url, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = self.SessionLocal()

    def create_database(self):
        """Creates all tables in the database."""
        Base.metadata.create_all(bind=self.engine)

    def add_user(self, username: str, hashed_password: str) -> bool:
        """
        Adds a new user to the database if not already present.

        Args:
            username (str): The username.
            hashed_password (str): The hashed password.

        Returns:
            bool: True if user added successfully, False otherwise.
        """
        try:
            user = self.get_user(username)
            if user:
                return False
            new_user = User(username=username, password=hashed_password)
            self.session.add(new_user)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def get_user(self, username: str, as_list=False) -> Union[User, List[str], None]:
        """
        Retrieves a user by username.

        Args:
            username (str): Username to search.
            as_list (bool): If True, returns user attributes as a list.

        Returns:
            User or list or None: User instance, list of attributes, or None.
        """
        user = self.session.query(User).filter(User.username == username).first()
        if not as_list:
            return user
        return self.user_object_to_list(user) if user else None

    def get_users(self) -> List[User]:
        """
        Retrieves all users from the database.

        Returns:
            list: A list of User objects.
        """
        return self.session.query(User).all()

    def change_user_password(self, username: str, new_hashed_password: str) -> bool:
        """
        Updates the password for a given user.

        Args:
            username (str): Username of the user.
            new_hashed_password (str): New hashed password.

        Returns:
            bool: True if update successful, False otherwise.
        """
        try:
            user = self.get_user(username)
            if user:
                user.password = new_hashed_password
                self.session.add(user)
                self.session.commit()
                return True  
            return False
        except Exception as e:
            print(e)
            return False

    def remove_user(self, username: str) -> bool:
        """
        Deletes a user from the database.

        Args:
            username (str): The username of the user to delete.

        Returns:
            bool: True if deletion successful, False otherwise.
        """
        try:
            user = self.get_user(username)
            if user:
                self.session.delete(user)
                self.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def add_item(self, item_name: str, quantity: int, price: float) -> bool:
        """
        Adds a new item to the inventory.

        Args:
            item_name (str): Item name.
            quantity (int): Quantity in stock.
            price (float): Price of the item.

        Returns:
            bool: True if item added, False if already exists.
        """
        item = self.get_item(item_name)
        if item:
            return False
        new_item = Item(name=item_name, quantity=quantity, price=price)
        self.session.add(new_item)
        self.session.commit()
        return True

    def get_item(self, item_name: str, as_list=False) -> Union[Item, List[Union[str, int, float]], None]:
        """
        Retrieves an item by name.

        Args:
            item_name (str): Name of the item.
            as_list (bool): If True, returns item attributes as a list.

        Returns:
            Item or list or None: The item object, attribute list, or None.
        """
        item = self.session.query(Item).filter(Item.name == item_name).first()
        if not as_list:
            return item
        return self.item_object_to_list(item) if item else None

    def get_items(self, as_list=False, cap=0) -> Union[List[Item], List[List[Union[str, int, float]]]]:
        """
        Retrieves multiple items.

        Args:
            as_list (bool): If True, returns list of item attribute lists.
            cap (int): Max number of items to retrieve (0 for all).

        Returns:
            list: List of Item objects or attribute lists.
        """
        items = self.session.query(Item).limit(cap).all() if cap else self.session.query(Item).all()
        if not as_list:
            return items
        return [self.item_object_to_list(item) for item in items]

    def update_item(self, item_name: str, quantity: int, price: float) -> bool:
        """
        Updates the quantity and price of an item.

        Args:
            item_name (str): Name of the item.
            quantity (int): New quantity.
            price (float): New price.

        Returns:
            bool: True if update successful, False otherwise.
        """
        item = self.get_item(item_name)
        try:
            if item:
                item.quantity = quantity
                item.price = price
                self.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def remove_item(self, item_name: str) -> bool:
        """
        Deletes an item from the inventory.

        Args:
            item_name (str): Name of the item to delete.

        Returns:
            bool: True if deletion successful, False otherwise.
        """
        try:
            item = self.get_item(item_name)
            if not item:
                return False
            self.session.delete(item)
            self.session.commit()
            return True 
        except Exception as e: 
            print(e)
            return False

    def user_object_to_list(self, user: User) -> List[str]:
        """
        Converts a User object to a list.

        Args:
            user (User): The user object.

        Returns:
            list: [username, password]
        """
        return [user.username, user.password]

    def item_object_to_list(self, item: Item) -> List[Union[str, int, float]]:
        """
        Converts an Item object to a list.

        Args:
            item (Item): The item object.

        Returns:
            list: [name, quantity, price]
        """
        return [item.name, item.quantity, item.price]

    def close_session(self):
        """
        Closes the current database session.
        """
        try:
            self.session.close()
        except Exception as e:
            print(f"Error closing session: {e}")