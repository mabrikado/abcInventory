import unittest
from .user_handler import *
import os

class TestUserHandler(unittest.TestCase):
    def setUp(self):
        self.filepath = "users.txt"
        self.user_handler = UserHandler(self.filepath)
        
        #create a file to text with
        with open(self.filepath , "w") as file:
            file.write("sibusiso abce90#\nsbuda edf9#\n")

    def test_read_user(self):
        self.assertEqual(["sibusiso" , "abce90#"] , self.user_handler.read_user("sibusiso"))

    def test_write_user(self):
        self.assertTrue(self.user_handler.write_user("mabrikado" , "99#"))
        self.assertEqual(["mabrikado" , "99#"] , self.user_handler.read_user("mabrikado"))

    def test_update_user(self):
        self.assertTrue(self.user_handler.write_user("sibusiso" , "newPassword23#" , True))
        self.assertEqual(["sibusiso" , "newPassword23#"] , self.user_handler.read_user("sibusiso"))
    
    def test_delete_user(self):
        self.assertTrue(self.user_handler.delete_user("sibusiso"))
        self.assertTrue(self.user_handler.delete_user("sbuda"))
    
    def test_is_file_empty(self):
        self.assertFalse(self.user_handler.is_file_empty())
        self.assertTrue(self.user_handler.delete_user("sibusiso"))
        self.assertTrue(self.user_handler.delete_user("sbuda"))
        self.assertTrue(self.user_handler.is_file_empty())

        #put wrong file
        self.user_handler.path = "sadsa.txt"
        with self.assertRaises(FileNotFoundError) as context:
            self.user_handler.is_file_empty()
    


    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        return 
    

if __name__ == "__main__":
    unittest.main()