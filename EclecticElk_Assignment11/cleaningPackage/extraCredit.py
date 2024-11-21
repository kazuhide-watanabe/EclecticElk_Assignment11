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
# Brief Description of what this module does: This file documents several issues with the data in the fuelPurchaseData.csv file. 
# Citations: In class notes, Bill Nicholson
# Anything else that's relevant:  This file was completed with contributions from everyone on the team.
#**********************************

# extraCredit.py

"""

- Full Address column has zip codes that are at the beginning of the string.

- In the Fuel Type column, liquid natural gas has multiple different names such as, “lng”, “LNG”, “liquid natural gas”, “liquified natural gas”, and “liquefied natural gas”.

- Values inside the Site ID column are a mixture of strings and integers depending on the Site Name. This could cause problems when trying to query by Site ID as a whole. 

- The Date & Time column does not use military time, am., or pm., so there is no way to distinguish whether it is before or after noon. 

"""
