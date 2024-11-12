# twoDecimal.py

import csv

# open and read csv data
with open('fuelPurchaseData.csv', mode = 'r', newline = '') as infile:

    reader = csv.reader(infile)
    header = next(reader)  # read the header row
    rows = list(reader) # real all rows

    # convert the column value to a float and format it to 2 decimal places
    columnName = 'Fuel Quantity'
    for row in rows:
        try:
            row[columnName] = "{:.2f}".format(float(row[columnName]))
        except ValueError:
            pass

    with open('cleanedData.csv', mode='w', newline='') as outfile:
        fieldnames = reader.fieldnames  # Get the fieldnames (headers) from the reader
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(rows)  # Write the modified rows
