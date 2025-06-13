import unittest
import file_handler
from Inventory import *
import os

class TestInvetory(unittest.TestCase):
    def setUp(self):
        self.filepath = "inventories.txt"
        self.inventory_handler = file_handler.InventoryHandler(self.filepath)
        self.database = DatabaseSQL("sqlite:///Inventory/inventory.db")
        self.inventoryFile = Inventory(self.inventory_handler)
        self.inventorySQL = Inventory(None , self.database)
        
        #create a file to text with
        with open(self.filepath , "w") as file:
            file.write("apple 5 8.5\nbanana 10 7.78\ngrape 8 12.4\n")
        
        self.database.create_database()
        self.database.add_item("apple" , 5 , 8.5)
        self.database.add_item("banana" , 10 , 7.78)
        self.database.add_item("grape" , 8 , 12.4)
    
    def test_inventory_exception(self):
        with self.assertRaises(InventoryException) as cm:
            Inventory()
    
    def test_item_value_file(self):
        self.assertEqual(42.5 , self.inventoryFile.item_total_value("apple"))
        self.assertEqual(77.8 , self.inventoryFile.item_total_value("banana"))
        self.assertEqual(99.2 , self.inventoryFile.item_total_value("grape"))
    
    def test_item_value_SQL(self):
        self.assertEqual(42.5 , self.inventorySQL.item_total_value("apple"))
        self.assertEqual(77.8 , self.inventorySQL.item_total_value("banana"))
        self.assertEqual(99.2 , self.inventorySQL.item_total_value("grape"))

    def test_items_with_total_file(self):
        self.assertEqual({'Name': ['apple', 'banana', 'grape'], 'Quantity': [5, 10, 8], 'Price': [8.5, 7.78, 12.4], 'Value': [42.5, 77.8, 99.2]},
                         self.inventoryFile.items_with_totals(0 , True , True))
    
    def test_items_with_total_SQL(self):
                self.assertEqual({'Name': ['apple', 'banana', 'grape'], 'Quantity': [5, 10, 8], 'Price': [8.5, 7.78, 12.4], 'Value': [42.5, 77.8, 99.2]},
                         self.inventorySQL.items_with_totals(0 , True , True))
    
    def test_total_inventory_value_file(self):
        self.assertEqual(219.5 , self.inventoryFile.total_inventory_value())
    
    def test_total_inventory_value_SQL(self):
        self.assertEqual(219.5 , self.inventorySQL.total_inventory_value())

    def test_read_items_ascending_file(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78]] , self.inventoryFile.read_items(2))
    
    def test_read_items_ascending_SQL(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78]] , self.inventorySQL.read_items(2))

    def test_read_all_items_file(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78] , ["grape" , 8 , 12.4]] , self.inventoryFile.read_items())
    
    def test_read_all_items_SQL(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78] , ["grape" , 8 , 12.4]] , self.inventorySQL.read_items())
    
    def test_read_item_file(self):
        self.assertEqual(["apple" , 5 , 8.5] , self.inventoryFile.read_item("apple"))
        self.assertIsNone(self.inventoryFile.read_item("orange"))
    
    def test_read_item_SQL(self):
        self.assertEqual(["apple" , 5 , 8.5] , self.inventorySQL.read_item("apple"))
        self.assertIsNone(self.inventorySQL.read_item("orange"))
    
    def test_add_item_file(self):
        self.assertTrue(self.inventoryFile.add_item("orange" , 10 , 12.4))
        self.assertEqual(["orange" , 10 , 12.4] , self.inventoryFile.read_item("orange"))
        self.assertFalse(self.inventoryFile.add_item("orange" , 10 , 12.4))
    
    def test_add_item_SQL(self):
        self.assertTrue(self.inventorySQL.add_item("orange" , 10 , 12.4))
        self.assertEqual(["orange" , 10 , 12.4] , self.inventorySQL.read_item("orange"))
        self.assertFalse(self.inventorySQL.add_item("orange" , 10 , 12.4))

    def test_update_item_file(self):
        self.assertTrue(self.inventoryFile.update_item("apple" , 20 , 7))
        self.assertEqual(["apple" , 20 , 7] , self.inventoryFile.read_item("apple"))
    
    def test_update_item_SQL(self):
        self.assertTrue(self.inventorySQL.update_item("apple" , 20 , 7))
        self.assertEqual(["apple" , 20 , 7] , self.inventorySQL.read_item("apple"))
    
    def test_remove_item_file(self):
        self.assertTrue(self.inventoryFile.remove_item("apple"))
        self.assertIsNone(self.inventoryFile.read_item("apple"))
    
    def test_remove_item_SQL(self):
        self.assertTrue(self.inventorySQL.remove_item("apple"))
        self.assertIsNone(self.inventorySQL.read_item("apple"))
    
    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        os.remove("Inventory/inventory.db")
        return 