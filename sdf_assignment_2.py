"""
Description: This project is resubmitted as a result of an academic integrity breach.The project provides coide sup[porting the outcomeof module2 in SDF.
Author: Armanjot kaur
Date: 20 october 2023
Usage:To calculate data type.
"""

# SIMPLE DATA TYPES
# Declare a variable to store a city
city = "Sri Muktsar Sahib"
print(f'value: {city} type: {type(city)}')



weekdays = "7"
print(f'value: {weekdays} type: {type(weekdays)}')





# CALCULATIONS

GST = 0.05
PST = 0.07
CP_Refridgerator = 2995.95
GST_ON_REFRIDGERATOR = CP_Refridgerator  * GST
PST_ON_REFRIDGERATOR = CP_Refridgerator * PST
PRICE = CP_Refridgerator + GST + PST
print(f"Refridgerator: ${CP_Refridgerator:.2f} , GST: ${GST_ON_REFRIDGERATOR:.2f} ,  PST: ${PST_ON_REFRIDGERATOR:.2f} ,  TOTAL: ${PRICE:.2f}")
 






# COLLECTIONS

lists = [1,5,22,7,23,86,12]

print(lists)

my_firstname = "Arman"
lists.insert(5, my_firstname)
print(lists)

lists.remove(7)
print(lists)

# TUPLES
courses = ("SDF" , "MATH" , "SERVICE MANAGEMENT" , "PROFESSIONAL DEVELOPMENT" , "INFORMATION SYSTEMS" , "COMMUNICATION STRATEGIES")
print(courses)

# DICTIONARIES 
nations = {"CANADA" : 38781291 , "USA" : 339986563 , "MEXICO" : 128465567}
print(nations)
# INDEX
nations["CANADA"] = 40000000

nations["BRAZIL"] = 216422446
print(nations)

# SETS
first_set = {1,17,54,21,12,77,23,12}
print(first_set)
second_set = {2,5,17,18,19,77,78,12}
print(second_set)
unique_set = first_set.union(second_set)
print(unique_set)
set = second_set.intersection(first_set)
print(set)
other_set = second_set.difference(first_set)
print(other_set)































































































































































































































































































# Armanjot



































