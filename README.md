# Batch Excel Merger With Custom Password

This script merges multiple Excel files from the current directory, adds custom password and batch number columns, and outputs a combined file.

## Features

- Merges all `.xlsx` and `.xls` files from the current directory.
- Adds a **custom password** (stored securely in GitHub Secrets as `CUSTOM_BATCH_PASSWORD`) based on file prefixes.
- Adds a **batch number** column to track records.
- Filters out example data (`範例1`, `範例2`) from the first column.

## Usage

1. **Set up GitHub Secrets**:
   - Add your custom password in the repository settings under **Secrets**.
     - Secret name: `CUSTOM_BATCH_PASSWORD`
   
2. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-url

3. **Run the script**:
   nsure your Excel files are placed in the current directory, then execute:
   ```python batch_excel_merger.py
     
4. **Output**:
   A new Excel file `merged_excel_with_custom_password_and_batch.xlsx` will be created, containing the merged data with custom password and batch number columns.

## Requirements

- Python 3.x
- Pandas
- OpenPyXL
