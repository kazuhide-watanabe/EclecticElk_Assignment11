#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton, Kyle Hsu
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
#         hsukt@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  11/21/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where a csv file needs to be cleaned up through certain instructions in order for it to be more presentable.
# Brief Description of what this module does: Creates a class called fridge and sets a default temperature for the fridge once it is plugged in. 
# After that you are able to change the temperature of the fidge between a cetain range. 
# Citations: In class notes, Bill Nicholson
# Anything else that's relevant:  This file was completed by Alex Carnes and Kazu Watanabe
#**********************************

# deletePepsi.py

import csv

def handle_pepsi_purchases(data, anomalies_path):
    """
    Remove rows where "Fuel Type" contains 'Pepsi' and save them to a separate CSV file.
    :param data: List of rows (including header).
    :param anomalies_path: Path to save the anomalies CSV.
    :return: List of cleaned rows (excluding 'Pepsi' rows).
    """
    header = data[0]
    fuel_type_index = header.index("Fuel Type")  # Locate the "Fuel Type" column

    # Separate Pepsi rows and non-Pepsi rows
    pepsi_rows = []
    cleaned_data = [header]  # Start with the header

    for row in data[1:]:
        # Normalize the "Fuel Type" value for comparison
        fuel_type = row[fuel_type_index].strip().lower()
        if "pepsi" in fuel_type:
            pepsi_rows.append(row)
        else:
            cleaned_data.append(row)

    # Write anomalies (Pepsi rows) to the anomalies CSV file
    with open(anomalies_path, mode='w', newline='') as anomalies_file:
        writer = csv.writer(anomalies_file)
        writer.writerow(header)  # Write the header
        writer.writerows(pepsi_rows)  # Write Pepsi rows

    return cleaned_data
