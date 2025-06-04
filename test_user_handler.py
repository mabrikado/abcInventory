import unittest
import file_handler
import os


class TestUserHandler(unittest.TestCase):
    def setUp(self):
        self.filepath = "users.txt"
        self.user_handler = file_handler.UserHandler(self.filepath)
        
        #create a file to text with
        with open(self.filepath , "w") as file:
            file.write("sibusiso abce90#\nsbuda edf9#\n")

    def test_read_user(self):
        self.assertEqual(["sibusiso" , "abce90#"] , self.user_handler.read_user("sibusiso"))
        
    def test_read_lines(self):
        self.assertEqual(["sibusiso abce90#\n" , "sbuda edf9#\n"] , file_handler.readlines(self.filepath))
        self.assertEqual(["sibusiso abce90#" , "sbuda edf9#"] , file_handler.readlines(self.filepath , True))

    def test_write_user(self):
        self.assertTrue(self.user_handler.write_user("mabrikado" , "99#"))
        self.assertEqual(["mabrikado" , "99#"] , self.user_handler.read_user("mabrikado"))

    def test_update_user(self):
        self.assertTrue(self.user_handler.write_user("sibusiso" , "newPassword23#" , True))
        self.assertEqual(["sibusiso" , "newPassword23#"] , self.user_handler.read_user("sibusiso"))
    
    def test_delete_user(self):
        self.assertTrue(self.user_handler.delete_user("sibusiso"))
        self.assertTrue(self.user_handler.is_file_empty())

    def test_clean_data(self):
        with open(self.filepath , "w") as file:
            file.write("\n\ndata1\ndata2\n\ndata3\n\ndata4\n")
        
        #clean data
        file_handler.clean_txt_data(self.filepath)

        #read new data
        with open(self.filepath , "r") as newFile:
            self.assertEqual("data1\ndata2\ndata3\ndata4\n" , newFile.read())

            


    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        return 
    

if __name__ == "__main__":
    unittest.main()