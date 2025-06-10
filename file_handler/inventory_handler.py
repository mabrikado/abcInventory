from typing import *
from utils import files

class InventoryHandler:
    def __init__(self , filepath):
        self.filepath = filepath
    
    @staticmethod
    def inventory_item_str_to_types(item:str) -> list:
        item_info = [""]
        counter_heading = 0 #count name of heading
        for char in item:
            if char == " ":
                item_info.append("")
                counter_heading+=1
            else:
                item_info[counter_heading] = item_info[counter_heading] + char
        item_info[1] = int(item_info[1])
        item_info[2] = float(item_info[2])
        
        return item_info
    
    @staticmethod
    def inventory_items_str_to_types(items:list) -> List[list]:
        types_items = []
        for item in items:
            types_items.append(InventoryHandler.inventory_item_str_to_types(item))
        return types_items
    
    def write_item(self , item_name:str ,  quantity:int , price:float , override:bool = False) -> bool:
        item = self.read_item(item_name)
        if item and not override:
            return False
        if override:
            self.delete_item(item_name)
        with open(self.filepath, "a") as file:
            file.write(f"{item_name} {quantity} {price}\n")    
        return True
    
    def read_item(self , item:str) -> str:
        with open(self.filepath , "r") as file:
            items = file.readlines()
            for line in items:
                if item in line:
                    # print(item.replace("\n" , ""))
                    return InventoryHandler.inventory_item_str_to_types(line)
    
    def read_items(self , cap:int = 0 , ascending_order = True):
        with open(self.filepath , "r") as file:
            items = file.readlines()
            if len(items) == 0:
                return None
            
            if not cap:
                cap = len(items)
            
            if ascending_order:
                return InventoryHandler.inventory_items_str_to_types(items[0:cap])
            items.reverse()
            type(cap)
            return InventoryHandler.inventory_items_str_to_types(items[0:cap])
    
    def delete_item(self , item_name:str):
        read_item = self.read_item(item_name)

        if not read_item:
            return False

        def exclude_item(item):
            return not item.startswith(item_name + " ") 

        users = files.readlines(self.filepath) 

        with open(self.filepath, "w") as file:
            file.writelines(filter(exclude_item, users))
        
        #clean data
        files.clean_txt_data(self.filepath)
        return True