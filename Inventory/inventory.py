from typing import *
from file_handler import InventoryHandler
from tabulate import tabulate
from colorama import Fore, Style, init

class Inventory:
    def __init__(self , inventoryhandler:InventoryHandler):
        self.inventoryhandler = inventoryhandler

    def add_item(self, item:str ,  quantity:int , price:float) -> bool:
        return self.inventoryhandler.write_item(item , quantity , price)

    def remove_item(self ,item:str) -> bool:
        return self.inventoryhandler.delete_item(item)

    def update_item(self , item:str ,  quantity:int , price:float) -> bool:
        return self.inventoryhandler.write_item(item , quantity , price , True)

    def read_item(self, item:str) -> list:
        return self.inventoryhandler.read_item(item)
    
    def read_items(self , cap:int = 0 , ascending_order = True) -> list:
        return self.inventoryhandler.read_items(cap , ascending_order)

    def item_total_value(self ,item , from_list=False) -> float:
        item = self.read_item(item) if not from_list else item
        return round(item[1] * item[2] , 2)

    
    def items_with_totals(self , cap=0 , ascending_order=True) ->list:
        items:List[list] = self.read_items(cap)
        for i in range(len(items)):
            items[i].append(self.item_total_value(items[i] , True))
        return items
        

    def total_inventory_value(self) -> float:
        items = self.read_items()
        total = 0
        for item in items:
            total += self.item_total_value(item[0])
        return total
    
    def display_items(self , cap:int=0 , ascending_order = True):
        init(autoreset=True)
        BOLD = '\033[1m'
        headers = [BOLD + "item" ,BOLD + "quantity" ,BOLD + "price" ,BOLD + "total"]
        items = self.items_with_totals()
        print(Fore.BLUE + tabulate(items, headers=headers, tablefmt="grid"))
        print(BOLD + Fore.BLUE + "Total Value :" + str(self.total_inventory_value()))