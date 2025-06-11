import os
import unittest
from excel import ExcelHandler  # Adjust import path if needed
from file_handler import InventoryHandler
from io import StringIO
import sys
from openpyxl import load_workbook


class TestExcelHandler(unittest.TestCase):
    def setUp(self):
        self.filepath = "inventories.txt"
        self.write_to_path = "excel/"

        # Ensure output directory exists
        os.makedirs(self.write_to_path, exist_ok=True)

        # Create test inventory file
        with open(self.filepath, "w") as file:
            file.write("apple 5 8.5\nbanana 10 7.78\ngrape 8 12.4\n")

        # Initialize handler and write inventory
        self.handler = ExcelHandler(self.filepath, self.write_to_path)
        self.handler.write_inventory()

        # Load the generated Excel workbook
        self.workbook = load_workbook(filename=os.path.join(self.write_to_path, "Inventory.xlsx"))
        self.worksheet = self.workbook["Inventory"]

    def test_write_file(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.handler.write_inventory()
        sys.stdout = sys.__stdout__

        expected_message = f"Excel file '{self.write_to_path}Inventory.xlsx' created successfully.\n"
        self.assertEqual(captured_output.getvalue(), expected_message)

    def test_sheet_heading(self):
        self.assertEqual(self.worksheet["A1"].value, "Inventory Information")

    def test_table_headings(self):
        self.assertEqual(self.worksheet["A3"].value, "Name")
        self.assertEqual(self.worksheet["B3"].value, "Quantity")
        self.assertEqual(self.worksheet["C3"].value, "Price")
        self.assertEqual(self.worksheet["D3"].value, "Value")

    def test_first_row(self):
        self.assertEqual(self.worksheet["A4"].value, "apple")
        self.assertEqual(self.worksheet["B4"].value, 5)
        self.assertEqual(self.worksheet["C4"].value, 8.5)
        self.assertEqual(self.worksheet["D4"].value, 42.5) 

    def test_second_row(self):
        self.assertEqual(self.worksheet["A5"].value, "banana")
        self.assertEqual(self.worksheet["B5"].value, 10)
        self.assertEqual(self.worksheet["C5"].value, 7.78)
        self.assertEqual(self.worksheet["D5"].value, 77.8)

    def test_third_row(self):
        self.assertEqual(self.worksheet["A6"].value, "grape")
        self.assertEqual(self.worksheet["B6"].value, 8)
        self.assertEqual(self.worksheet["C6"].value, 12.4)
        self.assertEqual(self.worksheet["D6"].value, 99.2)

    def test_total(self):
        self.assertEqual(self.worksheet["A7"].value, "Total")
        self.assertEqual(self.worksheet["D7"].value, 219.5)

    def tearDown(self):
        #Delete file after working with it
        os.remove("excel/Inventory.xlsx")
        return 