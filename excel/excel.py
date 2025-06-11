import pandas as pd
import Inventory
from file_handler import InventoryHandler


class ExcelHandler:
    """
    A class to handle writing inventory data to an Excel file using Pandas and XlsxWriter.
    
    Attributes:
        filepath (str): Path to the input inventory file.
        write_to_path (str): Directory path where the output Excel file will be saved.
        inventory (Inventory.Inventory): Loaded inventory object for data retrieval.
    """

    def __init__(self, filepath, write_to_path):
        """
        Initializes the ExcelHandler with a source inventory file and output directory.

        Args:
            filepath (str): Path to the input inventory file.
            write_to_path (str): Directory path where the output Excel file will be saved.
        """
        self.filepath = filepath
        self.inventory = Inventory.Inventory(InventoryHandler(filepath))
        self.write_to_path = write_to_path

    def write_inventory(self):
        """
        Writes the inventory data into an Excel file with formatting.

        The Excel file includes:
        - Merged header row with title "Inventory Information"
        - Formatted columns for quantity (integer), price, and total value (2 decimal places)
        - A total row at the end displaying the overall inventory value
        - Styled text and column widths for readability

        The resulting file is saved as 'Inventory.xlsx' in the specified output directory.
        """
        items = self.inventory.items_with_totals(0, True, True)
        df = pd.DataFrame(items)

        with pd.ExcelWriter(self.write_to_path + "Inventory.xlsx", engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Inventory', index=False, startrow=2)

            workbook = writer.book
            worksheet = writer.sheets['Inventory']

            merge_format = workbook.add_format({
                'bold': True,
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 14
            })
            worksheet.merge_range('A1:D1', 'Inventory Information', merge_format)

            format_qty = workbook.add_format({'num_format': '0', 'bold': True})
            worksheet.set_column('B:B', 10, format_qty)

            format_price = workbook.add_format({'num_format': '0.00', 'bold': True})
            worksheet.set_column('C:D', 15, format_price)

            start_row = 2
            n_rows = len(df)

            total_row = start_row + n_rows + 1
            worksheet.write(total_row, 0, 'Total', workbook.add_format({'bold': True}))
            worksheet.write(total_row, 3, self.inventory.total_inventory_value(),
                            workbook.add_format({'bold': True}))

        print(f"Excel file '{self.write_to_path}Inventory.xlsx' created successfully.")