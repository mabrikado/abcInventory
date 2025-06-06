from typing import *
from file_handler import InventoryHandler
from tabulate import tabulate
from colorama import Fore, Style, init

class Inventory:
    def __init__(self, inventoryhandler: InventoryHandler):
        self.inventoryhandler = inventoryhandler

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
        return self.inventoryhandler.write_item(item, quantity, price)

    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the inventory.

        Args:
            item (str): Name of the item to remove.

        Returns:
            bool: True if the item was successfully removed, False otherwise.
        """
        return self.inventoryhandler.delete_item(item)

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
        return self.inventoryhandler.write_item(item, quantity, price, True)

    def read_item(self, item: str) -> list:
        """
        Retrieve details of a single item from the inventory.

        Args:
            item (str): Name of the item to retrieve.

        Returns:
            list: Item details typically including name, quantity, and price.
        """
        return self.inventoryhandler.read_item(item)

    def read_items(self, cap: int = 0, ascending_order: bool = True) -> list:
        """
        Retrieve a list of items from the inventory.

        Args:
            cap (int, optional): Maximum number of items to retrieve.
                Defaults to 0 (no limit).
            ascending_order (bool, optional): Whether to sort items in ascending order.
                Defaults to True.

        Returns:
            list: List of items, each represented as a list of details.
        """
        return self.inventoryhandler.read_items(cap, ascending_order)

    def item_total_value(self, item, from_list: bool = False) -> float:
        """
        Calculate the total value of a single item (quantity * price).

        Args:
            item (str or list): Item name or item detail list.
            from_list (bool, optional): Whether the 'item' argument is already
                a list of item details. Defaults to False.

        Returns:
            float: Total value of the item rounded to two decimal places.
        """
        item = self.read_item(item) if not from_list else item
        return round(item[1] * item[2], 2)

    def items_with_totals(self, cap: int = 0, ascending_order: bool = True) -> list:
        """
        Retrieve all items including their total values.

        Args:
            cap (int, optional): Maximum number of items to retrieve.
                Defaults to 0 (no limit).
            ascending_order (bool, optional): Whether to sort items ascendingly.
                Defaults to True.

        Returns:
            list: List of items with an additional total value appended.
        """
        items: List[list] = self.read_items(cap, ascending_order)
        for i in range(len(items)):
            items[i].append(self.item_total_value(items[i], True))
        return items

    def total_inventory_value(self) -> float:
        """
        Calculate the total value of the entire inventory.

        Returns:
            float: Sum of total values of all items.
        """
        items = self.read_items()
        total = 0
        for item in items:
            total += self.item_total_value(item[0])
        return total

    def display_items(self, cap: int = 0, ascending_order: bool = True):
        """
        Display the inventory items in a formatted, colored table.

        Args:
            cap (int, optional): Maximum number of items to display.
                Defaults to 0 (display all).
            ascending_order (bool, optional): Whether to sort items ascendingly.
                Defaults to True.
        """
        init(autoreset=True)
        BOLD = '\033[1m'
        headers = [BOLD + "item", BOLD + "quantity", BOLD + "price", BOLD + "total"]
        items = self.items_with_totals(cap, ascending_order)
        print(BOLD + Fore.CYAN + "\nInventory of ABC Traders")
        print(Fore.BLUE + tabulate(items, headers=headers, tablefmt="grid"))
        print(BOLD + Fore.BLUE + "Total Value :" + str(self.total_inventory_value()))
