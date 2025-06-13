from typing import *
from file_handler import InventoryHandler
from tabulate import tabulate
from colorama import Fore, Style, init
from databaseSQL import *


class InventoryException(Exception):
    """
    Custom exception class for inventory-related errors.
    Raised when initialization or operations are performed with insufficient data sources.
    """
    pass


class Inventory:
    """
    A unified interface for managing an inventory, using either file-based or database-backed storage.

    Attributes:
        inventoryhandler (InventoryHandler): Handles file-based inventory operations.
        database (DatabaseSQL): Handles database-backed inventory operations.
    """

    def __init__(self, inventoryhandler: InventoryHandler = None, database: DatabaseSQL = None):
        """
        Initialize the inventory system with either a file handler or database.

        Args:
            inventoryhandler (InventoryHandler, optional): File-based handler for inventory data.
            database (DatabaseSQL, optional): Database interface for inventory data.

        Raises:
            InventoryException: If neither a file handler nor a database is provided.
        """
        if not inventoryhandler and not database:
            raise InventoryException("Is not provided with any data to read from")
        self.database = None
        if not database:
            self.inventoryhandler = inventoryhandler
        else:
            self.database = database

    def add_item(self, item: str, quantity: int, price: float) -> bool:
        """
        Add a new item to the inventory.

        Args:
            item (str): Name of the item to add.
            quantity (int): Quantity of the item.
            price (float): Price per unit of the item.

        Returns:
            bool: True if the item was successfully added, False otherwise.
        """
        return self.inventoryhandler.write_item(item, quantity, price) if not self.database else self.database.add_item(item, quantity, price)

    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the inventory.

        Args:
            item (str): Name of the item to remove.

        Returns:
            bool: True if the item was successfully removed, False otherwise.
        """
        return self.inventoryhandler.delete_item(item) if not self.database else self.database.remove_item(item)

    def update_item(self, item: str, quantity: int, price: float) -> bool:
        """
        Update an existing item's quantity and price.

        Args:
            item (str): Name of the item to update.
            quantity (int): New quantity of the item.
            price (float): New price per unit of the item.

        Returns:
            bool: True if the item was successfully updated, False otherwise.
        """
        return self.inventoryhandler.write_item(item, quantity, price, True) if not self.database else self.database.update_item(item, quantity, price)

    def read_item(self, item: str) -> list:
        """
        Retrieve details of a single item from the inventory.

        Args:
            item (str): Name of the item to retrieve.

        Returns:
            list: Item details [name, quantity, price], or an empty list if not found.
        """
        return self.inventoryhandler.read_item(item) if not self.database else self.database.get_item(item, True)

    def read_items(self, cap: int = 0, ascending_order: bool = True) -> list:
        """
        Retrieve a list of items from the inventory.

        Args:
            cap (int, optional): Maximum number of items to retrieve. Defaults to 0 (no limit).
            ascending_order (bool, optional): Whether to sort items in ascending order. Defaults to True.

        Returns:
            list: List of item detail lists, each containing [name, quantity, price].
        """
        if not ascending_order:
            if self.database:
                items = self.database.get_items(True, cap)
                items.reverse()
                return items
            else:
                return self.inventoryhandler.read_items(cap, False)
        return self.inventoryhandler.read_items(cap, True) if not self.database else self.database.get_items(True, cap)

    def item_total_value(self, item, from_list: bool = False) -> float:
        """
        Calculate the total value of a single item (quantity * price).

        Args:
            item (str or list): Item name (if from_list is False) or item data [name, quantity, price].
            from_list (bool, optional): Whether 'item' is already a list. Defaults to False.

        Returns:
            float: Total value of the item, rounded to two decimal places.
        """
        item = self.read_item(item) if not from_list else item
        return round(item[1] * item[2], 2)

    def items_with_totals(self, cap: int = 0, ascending_order: bool = True, as_dict: bool = False) -> Union[list, dict]:
        """
        Retrieve items with their total values (quantity * price).

        Args:
            cap (int, optional): Max number of items to retrieve. Defaults to 0 (no limit).
            ascending_order (bool, optional): Sort items in ascending order. Defaults to True.
            as_dict (bool, optional): Return data as a dictionary. Defaults to False.

        Returns:
            list or dict: List of items with total values appended, or dictionary format if as_dict is True.
        """
        items: List[list] = self.read_items(cap, ascending_order)
        items_dict = {"Name": [], "Quantity": [], "Price": [], "Value": []}

        for i in range(len(items)):
            value = self.item_total_value(items[i], True)

            if as_dict:
                items_dict["Name"].append(items[i][0])
                items_dict["Quantity"].append(items[i][1])
                items_dict["Price"].append(items[i][2])
                items_dict["Value"].append(value)
            else:
                items[i].append(value)

        return items_dict if as_dict else items

    def total_inventory_value(self) -> float:
        """
        Calculate the total value of all items in the inventory.

        Returns:
            float: Sum of all item values in inventory.
        """
        items = self.read_items()
        total = 0.0
        for item in items:
            total += self.item_total_value(item[0])
        return total

    def display_items(self, cap: int = 0, ascending_order: bool = True):
        """
        Display inventory items in a formatted table with color and totals.

        Args:
            cap (int, optional): Max number of items to display. Defaults to 0 (all items).
            ascending_order (bool, optional): Sort items in ascending order. Defaults to True.

        Output:
            Prints a table of inventory items and their total values to the console.
        """
        init(autoreset=True)
        BOLD = '\033[1m'
        headers = [BOLD + "item", BOLD + "quantity", BOLD + "price", BOLD + "total"]
        items = self.items_with_totals(cap, ascending_order)
        print(BOLD + Fore.CYAN + "\nInventory of ABC Traders")
        print(Fore.BLUE + tabulate(items, headers=headers, tablefmt="grid"))
        print(BOLD + Fore.BLUE + "Total Value :" + str(self.total_inventory_value()))

