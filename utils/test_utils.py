import unittest
from . import *
import os

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.filepath = "file.txt"
        with open(self.filepath , "w") as file:
            file.writelines(["data1\n" , "data2\n" , "data3\n" , "data4\n"])
    
    def test_clean_data(self):
        with open(self.filepath , "w") as file:
            file.write("\n\ndata1\ndata2\n\ndata3\n\ndata4\n")
        
        clean_txt_data(self.filepath)

        #clean data
        with open(self.filepath , "r") as file:
            self.assertEqual("data1\ndata2\ndata3\ndata4\n" , file.read())
    
    def test_read_files(self):
        self.assertEqual(["data1\n" , "data2\n" , "data3\n" , "data4\n"] , readlines(self.filepath))
    
    def test_read_files(self):
        self.assertEqual(["data1" , "data2" , "data3" , "data4"] , readlines(self.filepath , True))
    
    def testregistration_key(self):
        with open(self.filepath , "w") as file:
            file.write("REG-ABC123-XYZ")
        self.assertEqual("REG-ABC123-XYZ" , registration_key(self.filepath))
    
    def tearDown(self):
        #Delete file after working with it
        os.remove(self.filepath)
        return 


    
if __name__ == "__main__":
    unittest.main()