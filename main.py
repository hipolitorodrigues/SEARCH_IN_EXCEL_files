import tkinter as tk
from tkinter import filedialog, scrolledtext
import pandas as pd

# =======================
# Model - Data and Logic
# =======================
class ExcelSearchApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("hipolitorodrigues - Search in Excel Files")
        self.root.geometry("600x400")
        self.root.minsize(500, 300)

        # loading icon (Only for Windows)
        try:
            self.root.iconbitmap("./assets/images/icon-bar.ico")  # Uses .ico for Windows
        except tk.TclError:
            pass  # Remove the fallback for Linux/Mac

        # List to store the loaded files
        self.filepaths = []
        
        # Creating widgets
        self.create_widgets()

# =======================
# View - Graphical Interface
# =======================
    def create_widgets(self):
        """Creates the graphical interface widgets."""
        
        # Search field
        self.entry_search = tk.Entry(self.root, font=("Arial", 12))
        self.entry_search.pack(fill=tk.X, padx=10, pady=5)
        
        # Search button
        self.btn_search = tk.Button(self.root, text="Search", command=self.search, font=("Arial", 12))
        self.btn_search.pack(fill=tk.X, padx=10, pady=5)
        
        # Button to load files
        self.btn_load = tk.Button(self.root, text="Load Excel Files", command=self.load_files, font=("Arial", 12))
        self.btn_load.pack(fill=tk.X, padx=10, pady=5)
        
        # Results display area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)

# =======================
# Controller - Application Logic
# =======================
    def load_files(self):
        """Opens the dialog box to select Excel files and stores them."""
        filepaths = filedialog.askopenfilenames(filetypes=[("Excel Files", "*.xlsx")])
        if filepaths:
            self.filepaths = filepaths
            self.text_area.insert(tk.END, f"{len(filepaths)} file(s) successfully loaded!\n")

    def search(self):
        """Performs the search for the entered term in all sheets of the loaded files."""
        term = self.entry_search.get().strip().lower()
        if not term:
            self.text_area.insert(tk.END, "Please enter a term to search.\n")
            return
        
        if not self.filepaths:
            self.text_area.insert(tk.END, "No files loaded.\n")
            return
        
        self.text_area.delete(1.0, tk.END)  # Clears the text area
        
        for filepath in self.filepaths:
            xls = pd.ExcelFile(filepath)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)  # Converts all columns to string
                df = df.fillna('')  # Replaces NaN values with empty strings
                for _, row in df.iterrows():
                    row_text = ' '.join(row.astype(str).str.lower())  # Joins the entire row as a string
                    if term in row_text:
                        self.text_area.insert(tk.END, f"File: {filepath}\n")
                        self.text_area.insert(tk.END, f"Sheet: {sheet_name}\n")
                        for col in df.columns:
                            self.text_area.insert(tk.END, f" || {col} ||: {row[col]}\n")
                        self.text_area.insert(tk.END, "-_" * 30 + "\n" * 2)

# Calling the app
""" if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelSearchApp(root)
    root.mainloop() """

# or

def main():
    root = tk.Tk()
    app = ExcelSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
