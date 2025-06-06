import unittest
import file_handler
from Inventory import User
import os


class TestUser(unittest.TestCase):
        def setUp(self):
            self.filepath = "users.txt"
            self.user_handler = file_handler.UserHandler(self.filepath)
            self.user = User("mabrikado" , "abc#" , self.user_handler)
            #create a file to text with
            with open(self.filepath , "w") as file:
                file.write("sibusiso abce90#\nmabrikado abc#\n")
        
        def test_create_user(self):
            self.assertEqual(User("MegaSbu" , "boy77" , self.user_handler) , User.create_user("MegaSbu" , "boy77" , self.user_handler))
            self.assertEqual(["MegaSbu" , "boy77"] , self.user_handler.read_user("MegaSbu"))
            self.assertIsNone(User.create_user("MegaSbu" , "boy77" , self.user_handler))
        
        def test_change_password(self):
            self.assertTrue(self.user.change_password("abc#" , "ff4#"))
            self.assertEqual(["mabrikado" , "ff4#"] , self.user_handler.read_user("mabrikado"))
            self.assertFalse(self.user.change_password("asdsad#" , "asdsa#"))
            self.assertEqual(["mabrikado" , "ff4#"] , self.user_handler.read_user("mabrikado"))
            
        def test_log_user(self):
            self.assertEqual(User("sibusiso" , "abce90#" , self.user_handler) , User.log_user("sibusiso" , "abce90#" , self.user_handler))
            self.assertIsNone(User.log_user("sibusissdfdso" , "abce90#" , self.user_handler))
            self.assertIsNone(User.log_user("sibusissdfdso" , "abce90safdsf#" , self.user_handler))
        
        def test_delete_user(self):
            self.assertFalse(self.user.delete_user("sdfdsfds"))
            self.assertTrue(self.user.delete_user("abc#"))
            self.assertFalse(self.user.delete_user("abc#"))
        
        def tearDown(self):
            #Delete file after working with it
            os.remove(self.filepath)
            return 
        
if __name__ == "__main__":
    unittest.main()