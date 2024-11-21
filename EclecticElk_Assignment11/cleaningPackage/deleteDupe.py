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
# Brief Description of what this module does: This file ensures that any rows in the csv file that are duplicates of another are deleted. 
# Citations: In class notes, Bill Nicholson, ChatGPT
# Anything else that's relevant:  This file was completed by Alex Patton and Kazu Watanabe
#**********************************

# deleteDupe.py

def delete_duplicates(data):
    """
    Remove duplicate rows from the data.
    :param data: List of rows (including header).
    :return: List of unique rows (including header).
    """
    seen = set()
    unique_data = []
    for row in data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            unique_data.append(row)
            seen.add(row_tuple)
    return unique_data
