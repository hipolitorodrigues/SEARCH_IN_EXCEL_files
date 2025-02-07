<div align="center">
   <img height="30" width="40" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-ico.svg">
   <a href="./README.md">
      <img height="30" width="120" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-en.svg">
   </a>
   <a href="./README.pt-BR.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-pt-br.svg">
   </a>
</div>

# Search in Excel Files

## About the Project

**Search in Excel Files** is a desktop application developed in **Python 3.13.1** using the **Tkinter** library for the graphical interface. Its purpose is to allow users to load multiple **.xlsx** files and search across all their sheets, displaying the results in an organized manner.

![alt text](https://github.com/hipolitorodrigues/assets-for-github/blob/d34a7a288e52f24ee194872375c59bf88b02abc6/images/01/screenshot-02.png)

## Features

- **Load multiple Excel (.xlsx) files simultaneously**
- **Search for a term in all sheets of all loaded files**
- **Display formatted results in the graphical interface**
- **Responsive and user-friendly interface**

## Technologies Used

- **Python 3.13.1**
- **Tkinter** - Graphical interface
- **Pandas** - Data manipulation for Excel files
- **Pyinstaller** - Creation of a portable exe version

## How to Run

**METHOD 1**
1. Make sure you have Python 3.13.1 installed.
2. Install the necessary dependencies by running:
   ```sh
   pip install pandas openpyxl tk
   ```
3. Run the application with the command:
   ```sh
   python main.py
   ```
**METHOD 2**
1. Open the `portable_exe_version` folder.
2. Double-click the portable exe file `Search_in_Excel_Files.exe`.

## How to Use

1. **Open the application** - Run the `main.py` script or the portable exe file `Search_in_Excel_Files.exe`.
2. **Load files** - Click the **"Load Excel Files"** button and select the desired files.
3. **Perform a search** - Enter a term in the search field and click the **"Search"** button.
4. **View results** - The results will be displayed in the text area of the interface, showing:
   - The file where the term was found
   - The corresponding sheet
   - The row containing the found term

## Code Structure

The project follows **SOLID** principles, using the **MVC (Model-View-Controller)** pattern:

- **Model:** `ExcelSearchApp` class, which manages the loaded files and search logic.
- **View:** `create_widgets()` module, which defines the graphical interface elements.
- **Controller:** `load_files()` and `search()` methods, which handle user interactions and file searches.

## Possible Future Improvements

- Add support for **.csv** and **.xls** files.
- Option to export search results to a text or Excel file.
- Interface improvements using **ttk** for a more modern design.

## Author

- **Developer**: Hipolito Rodrigues
- **Creation Date**: 02/04/2025
- **Last Update**: 02/06/2025
- **Current Version**: 0.94

---

## License

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as you retain the original copyright notice and include the license in all copies or substantial portions of the software.
