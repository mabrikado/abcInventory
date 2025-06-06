import unittest
import file_handler
import os

class TestInventoryHandler(unittest.TestCase):
    def setUp(self):
        self.filepath = "inventories.txt"
        self.inventory_handler = file_handler.InventoryHandler(self.filepath)
        
        #create a file to text with
        with open(self.filepath , "w") as file:
            file.write("apple 5 8.5\nbanana 10 7.78\ngrape 8 12.4\n")
        
    
    def test_inventory_str_to_types(self):
        self.assertEqual(["apple" , 5 , 8.5] , file_handler.InventoryHandler.inventory_item_str_to_types("apple 5 8.5"))
        self.assertEqual(["banana" , 10 , 7.78] , file_handler.InventoryHandler.inventory_item_str_to_types("banana 10 7.78"))
        
    def test_inventory_str_to_types(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78]] , file_handler.InventoryHandler.inventory_items_str_to_types(["apple 5 8.5" , "banana 10 7.78"]))

    def test_read_items_ascending(self):
        self.assertEqual([["apple" , 5 , 8.5] , ["banana" , 10 , 7.78]] , file_handler.InventoryHandler.read_items(self.inventory_handler , 2))
    
    def test_read_items_decending(self):
        self.assertEqual([["grape" , 8 , 12.4] , ["banana" , 10 , 7.78]] , file_handler.InventoryHandler.read_items(self.inventory_handler , 2 , False))

    def test_read_all_items(self):
        self.assertEqual([["apple" ,  5 , 8.5] , ["banana" , 10 , 7.78] , ["grape" , 8 , 12.4]] , file_handler.InventoryHandler.read_items(self.inventory_handler))
    
    
    def test_read_item(self):
        self.assertEqual(["apple" , 5 , 8.5] , self.inventory_handler.read_item("apple"))
        self.assertIsNone(self.inventory_handler.read_item("orange"))
    
    def test_write_item(self):
        self.assertTrue(self.inventory_handler.write_item("orange" , 10 , 12.4))
        self.assertEqual(["orange" , 10 , 12.4] , self.inventory_handler.read_item("orange"))
        self.assertFalse(self.inventory_handler.write_item("apple" , 12 , 89))
    
    def test_update_item(self):
        self.assertTrue(self.inventory_handler.write_item("apple" , 20 , 7 , True))
        self.assertEqual(["apple" , 20 , 7] , self.inventory_handler.read_item("apple"))
    
    def test_delete_item(self):
        self.assertTrue(self.inventory_handler.delete_item("apple"))
        self.assertIsNone(self.inventory_handler.read_item("apple"))
    
    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        return 
    

if __name__ == "__main__":
    unittest.main()