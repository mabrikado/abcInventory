import unittest
import file_handler
from Inventory import *

import os

class TestInvetory(unittest.TestCase):
    def setUp(self):
        self.filepath = "inventories.txt"
        self.inventory_handler = file_handler.InventoryHandler(self.filepath)
        self.inventoryClass = Inventory(self.inventory_handler)
        
        #create a file to text with
        with open(self.filepath , "w") as file:
            file.write("apple 5 8.5\nbanana 10 7.78\ngrape 8 12.4\n")
    
    def test_item_value(self):
        self.assertEqual(42.5 , self.inventoryClass.item_total_value("apple"))
        self.assertEqual(77.8 , self.inventoryClass.item_total_value("banana"))
        self.assertEqual(99.2 , self.inventoryClass.item_total_value("grape"))
    
    def test_total_inventory_value(self):
        self.assertEqual(219.5 , self.inventoryClass.total_inventory_value())
    
    def test_read_items_ascending(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78]] , self.inventoryClass.read_items(2))
    
    def test_read_items_decending(self):
        self.assertEqual([["grape" , 8 , 12.4] , ["banana" , 10 , 7.78]] , self.inventoryClass.read_items(2 , False))

    def test_read_all_items(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78] , ["grape" , 8 , 12.4]] , self.inventoryClass.read_items())
    
    
    def test_read_item(self):
        self.assertEqual(["apple" , 5 , 8.5] , self.inventoryClass.read_item("apple"))
        self.assertIsNone(self.inventoryClass.read_item("orange"))
    
    def test_add_item(self):
        self.assertTrue(self.inventoryClass.add_item("orange" , 10 , 12.4))
        self.assertEqual(["orange" , 10 , 12.4] , self.inventoryClass.read_item("orange"))
        self.assertFalse(self.inventoryClass.add_item("orange" , 10 , 12.4))
    
    def test_update_item(self):
        self.assertTrue(self.inventoryClass.update_item("apple" , 20 , 7))
        self.assertEqual(["apple" , 20 , 7] , self.inventoryClass.read_item("apple"))
    
    def test_remove_item(self):
        self.assertTrue(self.inventoryClass.remove_item("apple"))
        self.assertIsNone(self.inventoryClass.read_item("apple"))
    
    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        return 