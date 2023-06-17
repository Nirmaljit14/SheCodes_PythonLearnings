import csv
# Lists = []

# dictionary
# TKey:TValue
# Keys are immuatble datatype
# Values can be any datatypes
# immutable - Strings, integers, floats, double, booleans

# studemt_phonebook = {
#     "Nj":111,
#     "Ayushi":222,
#     "Jenny":333,
#     "Tracey":444,
#     "Claire":555
#}
# gets values based on keys
# for key in studemt_phonebook:
#     print(key, studemt_phonebook[key])

# # gets values using .value() function
# for value in studemt_phonebook.values():
#     print(value)

# # use to unpacking
# for example in studemt_phonebook.items():
#     print(example)


# # adding/updating values in dictionary
# studemt_phonebook["yara"] = 666
# print(studemt_phonebook)
# del studemt_phonebook["Nj"]
# print(studemt_phonebook)

# Q1The dictionary below represents the cost of individual items in a supermarket. 
# Write aprogram that asks the user how many of each item they would like in turn, 
# and outputsthe total cost of their groceries.
unit_total = 0
groceries = {
    "babby-spinach": 2.78,
    "Hot Chocolate":3.70,
    "Crackers":2.10,
    "Roti": 12.0,
    "Cauliflower": 2.90
}

for key, value in groceries.items():
    numbers = int(input(f"pleae input the number of items you want{key}"))
    print(numbers)
    total = numbers * value
    unit_total += total
print(unit_total) 

# Q2 In the last lesson, you wrote a program that counted the number of colour names inthe colours_865.csv file.
# Try rewriting this program so that instead of using separate variables to keep track ofthe number of times each colour name appears,
# it uses a single dictionary instead.Here's a dictionary to get you started:

# colours_dict = {}
# with open(file="Session6/colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file, delimiter=",")
#     for row in csv_reader:
#         print(row)
#         colours_dict[row[1]] = row[2]
#         print(colours_dict)