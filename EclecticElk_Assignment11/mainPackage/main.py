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
# Brief Description of what this module does: This file calls all the files in the cleaningPackage, loads the dataset, and saves all the changes into different csv files 
# # as instructed by the code  
# Citations: In class notes, Bill Nicholson, ChatGPT
# Anything else that's relevant:  This file was completed by Kazu Watanabe
#**********************************

# main.py

import csv
from cleaningPackage.deleteDupe import *
from cleaningPackage.deletePepsi import *
from cleaningPackage.twoDecimal import *
from cleaningPackage.updateZip import *


def main():
    """
    Orchestrates the entire data cleaning process:
    """
    # Paths to data files
    input_csv = 'Data/fuelPurchaseData.csv'
    anomalies_csv = 'Data/dataAnomalies.csv'
    cleaned_csv = 'Data/cleanedData.csv'
    missing_zip_csv = 'Data/missingZipAddresses.csv'

    # Load the dataset
    with open(input_csv, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Step 1: Format "Gross Price" to two decimal places
    data = format_gross_price(data)

    # Step 2: Remove rows with Pepsi purchases and log them to dataAnomalies.csv
    data = handle_pepsi_purchases(data, anomalies_csv)

    # Step 3: Remove duplicate rows
    data = delete_duplicates(data)

    # Save cleaned data
    with open(cleaned_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Data cleanup completed. Cleaned data saved to:", cleaned_csv)
    
    
    # Process the data to find addresses missing zip codes
    extract_missing_zip_addresses(data, missing_zip_csv)
    print(f"Missing zip addresses written to {missing_zip_csv}")

    # Update missing zip codes
    update_missing_zip_addresses(data, missing_zip_csv, cleaned_csv)

if __name__ == "__main__":
    main()
