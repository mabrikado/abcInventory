import unittest
import file_handler
from Inventory import User
import os
import bcrypt


class TestUser(unittest.TestCase):
        def setUp(self):
            self.filepath = "users.txt"
            self.user_handler = file_handler.UserHandler(self.filepath)
            self.user = User("mabrikado" , "abc#" , self.user_handler)
            #create a file to text with
            with open(self.filepath , "w") as file:
                # abce90# -> $2b$12$BT7S/j07Qnrsz5OOvi33S.IZq9eL6Bm1Wjof0CS2q26tATHXwkPEe
                # abc# -> $2b$12$d46u3.Ay1ADynyIILOX6H.vI6JNZDYKuFbPwbSaTirtnS8brgT89e
                file.write("sibusiso $2b$12$BT7S/j07Qnrsz5OOvi33S.IZq9eL6Bm1Wjof0CS2q26tATHXwkPEe\nmabrikado $2b$12$d46u3.Ay1ADynyIILOX6H.vI6JNZDYKuFbPwbSaTirtnS8brgT89e\n")
        
        def test_create_user(self):
            self.assertEqual(User("MegaSbu" , "boy77" , self.user_handler) , User.create_user("MegaSbu" , "boy77" , self.user_handler))
            user = self.user_handler.read_user("MegaSbu")
            self.assertEqual("MegaSbu" , user[0])
            self.assertTrue(bcrypt.checkpw("boy77".encode("utf-8") , user[1].encode('utf-8')))
            self.assertIsNone(User.create_user("MegaSbu" , "boy77" , self.user_handler))
        
        def test_change_password(self):
            self.assertTrue(self.user.change_password("abc#" , "ff4#"))
            user = self.user_handler.read_user("mabrikado")
            self.assertEqual("mabrikado" , user[0])
            self.assertTrue(bcrypt.checkpw("ff4#".encode("utf-8") , user[1].encode('utf-8')))
            self.assertFalse(self.user.change_password("asdsad#" , "asdsa#"))
            user = self.user_handler.read_user("mabrikado")
            self.assertTrue(bcrypt.checkpw("ff4#".encode("utf-8") , user[1].encode('utf-8'))) #check that nothing changed
            
        def test_log_user(self):
            self.assertEqual(User("sibusiso" , "abce90#" , self.user_handler) , User.log_user("sibusiso" , "abce90#" , self.user_handler))
            self.assertIsNone(User.log_user("sibusissdfdso" , "abce90#" , self.user_handler))
            self.assertIsNone(User.log_user("sibusissdfdso" , "abce90safdsf#" , self.user_handler))
        
        def test_delete_user(self):
            self.assertFalse(self.user.delete_user("sdfdsfds"))
            self.assertTrue(self.user.delete_user("abc#"))
            self.assertFalse(self.user.delete_user("abc#"))
        
        def test_str_(self):
            self.assertEqual("mabrikado" , str(self.user))
        
        def tearDown(self):
            #Delete file after working with it
            os.remove(self.filepath)
            return 
        
if __name__ == "__main__":
    unittest.main()