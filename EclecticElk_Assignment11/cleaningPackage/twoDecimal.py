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
# Brief Description of what this module does: This module cleans the "Gross Price" column of the csv file by making it so that all values in the row are two decimal places. 
# Citations: In class notes, Bill Nicholson, ChatGPT
# Anything else that's relevant:  This file was completed by Kyle Hsu and Kazu Watanabe
#**********************************

# twoDecimal.py

def format_gross_price(data):
    """
    Ensure the "Gross Price" column values have exactly two decimal places.
    If a number has only one decimal place, append '0' to make it two.
    :param data: List of rows (including header).
    :return: Updated data with formatted "Gross Price".
    """
    header = data[0]
    gross_price_index = header.index("Gross Price")  # Locate the "Gross Price" column

    formatted_data = [header]  # Start with the header row
    for row in data[1:]:
        price = row[gross_price_index].strip()  # Clean up leading/trailing spaces
        if '.' in price:
            # Split the price into whole and decimal parts
            whole, decimal = price.split('.')
            if len(decimal) == 1:  # Check if there's only one decimal digit
                price = f"{whole}.{decimal}0"  # Add a trailing '0'
        else:
            # If no decimal point exists, treat it as a whole number
            price = f"{price}.00"
        row[gross_price_index] = price
        formatted_data.append(row)

    return formatted_data
