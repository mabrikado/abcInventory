from typing import *

class Inventory:
    def __init__(self , filepath):
        self.filepath = filepath

    def add_item(item:str ,  quantity:int , price:float) -> None:
        pass

    def remove_item(item:str):
        pass

    def update_item(item:str ,  quantity:int , price:float):
        pass

    def read_item(item:str) -> List[Union[str , int , float]]:
        pass

    def read_all() -> dict:
        pass

