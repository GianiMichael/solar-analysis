"""
combine_net_metering.py
 
Combines EIA Form 861 Net Metering Excel files (2015-2024) into one CSV.
Handles the 2015 column order mismatch by reordering columns to match later years.
"""
 
import os
import csv
import openpyxl
 
folder = r'C:\Users\gianc\Downloads'
output = r'C:\Users\gianc\Downloads\combined_net_metering.csv'
 
# Collect all Net Metering xlsx files in sorted order
files = sorted([
    f for f in os.listdir(folder)
    if f.startswith('Net_Metering_') and f.endswith('.xlsx')
])
 
with open(output, 'w', newline='', encoding='utf-8') as outfile:
    writer = None
 
    for i, fname in enumerate(files):
        print(f'Processing: {fname}')
        wb = openpyxl.load_workbook(os.path.join(folder, fname), data_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
 
        if i == 0:
            # Write header + all rows from first file
            writer = csv.writer(outfile)
            writer.writerows(rows)
        else:
            # Skip header row for subsequent files
            writer.writerows(rows[1:])
 
        print(f'Done: {fname}')
 
print(f'Combined file saved to: {output}')
