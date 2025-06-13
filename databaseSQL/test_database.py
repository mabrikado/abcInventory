import unittest
import os
from .database import *

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.databaseUrl = "sqlite:///databaseSQL/inventory.db"
        self.database = DatabaseSQL(self.databaseUrl)
        self.database.create_database()

    def test_add_user(self):
        self.assertTrue(self.database.add_user("sbuda" , "unhashed99"))
        self.assertFalse(self.database.add_user("sbuda" , "unhashed99"))
    
    def test_get_user(self):
        self.test_add_user()
        self.assertEqual(User(username="sbuda" , password="unhashed99") , self.database.get_user("sbuda"))
    
    def test_get_user_as_list(self):
        self.test_add_user()
        self.assertEqual(["sbuda" , "unhashed99"] , self.database.get_user("sbuda" , True))
    
    def test_get_users(self):
        self.assertTrue(self.database.add_user("sbuda" , "eeyuh"))
        self.assertTrue(self.database.add_user("mxo" , "yebo"))
        expected_list = [User(username="sbuda" , password="eeyuh") , User(username="mxo" , password="yebo")]
        actual_list = self.database.get_users()
        self.assertEqual(expected_list , actual_list)
    
    def test_remove_user(self):
        self.test_add_user()
        self.assertTrue(self.database.remove_user("sbuda"))
        self.assertIsNone(self.database.get_user("sbuda"))
    
    def test_change_password(self):
        self.test_add_user()
        self.assertTrue(self.database.change_user_password("sbuda" , "newPass"))
        self.assertEqual(User(username="sbuda" , password="newPass") , self.database.get_user("sbuda"))
        self.assertFalse(self.database.change_user_password("mxo" , "hjui8"))
    
    def test_add_item(self):
        self.assertTrue(self.database.add_item("apple" , 5 , 12.45))
        self.assertFalse(self.database.add_item("apple" , 5 , 12.45))
    
    def test_get_item(self):
        self.test_add_item()
        self.assertEqual(Item(name="apple" , quantity=5 , price=12.45) , self.database.get_item("apple"))

    def test_get_item_as_list(self):
        self.test_add_item()
        self.assertEqual(["apple" , 5 , 12.45] , self.database.get_item("apple" , True))
    
    def test_get_items_as_list(self):
        self.test_add_item()
        self.assertTrue(self.database.add_item("banana" , 12 , 34.23))
        expected_list = [["apple" , 5 , 12.45] , ["banana" , 12 , 34.23]]
        self.assertEqual(expected_list , self.database.get_items(True))
    
    def test_get_items(self):
        self.test_add_item()
        self.assertTrue(self.database.add_item("banana" , 12 , 34.23))
        expected_list = [Item(name="apple" , quantity=5 , price=12.45) , Item(name="banana" , quantity=12 , price=34.23)]
        self.assertEqual(expected_list , self.database.get_items())


    def test_remove_item(self):
        self.test_add_item()
        self.assertTrue(self.database.remove_item("apple"))
        self.assertIsNone(self.database.get_item("apple"))
    
    def test_change_items(self):
        self.test_add_item()
        self.assertTrue(self.database.update_item("apple" , 23 , 34.34))
        self.assertEqual(Item(name="apple" , quantity=23 , price=34.34) , self.database.get_item("apple"))

    
    def tearDown(self):
        self.database.close_session()
        os.remove("databaseSQL/inventory.db")

if __name__ == "__main__":
    unittest.main()