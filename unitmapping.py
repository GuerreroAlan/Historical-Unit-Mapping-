import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

class CSVMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Merger App")

        # Labels
        self.label1 = tk.Label(root, text="Select the Historic Unit Export CSV file:")
        self.label1.pack(pady=10)

        self.file1_path = tk.Entry(root, width=50)
        self.file1_path.pack(pady=5)

        self.browse_button1 = tk.Button(root, text="Browse", command=self.browse_file1)
        self.browse_button1.pack(pady=5)

        self.label2 = tk.Label(root, text="Select the Actual Unit Export CSV file:")
        self.label2.pack(pady=10)

        self.file2_path = tk.Entry(root, width=50)
        self.file2_path.pack(pady=5)

        self.browse_button2 = tk.Button(root, text="Browse", command=self.browse_file2)
        self.browse_button2.pack(pady=5)

        self.merge_button = tk.Button(root, text="Merge CSV Files", command=self.merge_csv)
        self.merge_button.pack(pady=20)

        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=10)

    def browse_file1(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file1_path.delete(0, tk.END)
        self.file1_path.insert(0, filename)

    def browse_file2(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file2_path.delete(0, tk.END)
        self.file2_path.insert(0, filename)

    def merge_csv(self):
        file1 = self.file1_path.get()
        file2 = self.file2_path.get()

        try:
            df1 = pd.read_csv(file1)  # Load first CSV
            df2 = pd.read_csv(file2)  # Load second CSV

            # Merge the DataFrames on the "UnitName" column
            merged_df = pd.merge(df1, df2, on='UnitName', how='inner')

            # Select only the UnitID_x and UnitID_y columns
            merged_df = merged_df[['UnitID_x', 'UnitID_y']]

            # Rename the columns
            merged_df.columns = ['Historic Qualtrics Unit ID', 'Current Qualtrics Unit ID']

            # Specify the output filename with a timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")  # Format: YYYYMMDD_HHMMSS
            output_filename = f'UnitMapping_mix_{timestamp}.csv'

            # Save the merged DataFrame to a new CSV file
            merged_df.to_csv(output_filename, index=False)

            self.status_label.config(text=f'Merged DataFrame saved as: {output_filename}')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVMergerApp(root)
    root.mainloop()