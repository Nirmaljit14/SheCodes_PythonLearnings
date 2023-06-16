import csv

# Q1Write a program that reads in colours_20_simple.csv 
# and print each line of the colourdata one by one as a string. 
# Use spaces to separate the columns insead of commas.

# with open(file="Session5/colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file, delimiter=" ")
#     for row in csv_reader:
#         print(row)

# Q2 Write a program that reads in colours_20_simple.csv 
# and outputs the colour data inorder English, Hex then RGB


with open(file="Session5/colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.reader(my_file, delimiter=" ")
    for row in csv_reader:
        print(row)

# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow("Hello")

# with open(file="Session5/galaxies.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

# population = []

# with open(file="Session5/galaxies.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         population.append(line)


# with open(file+"population.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file,delimiter="-")


    # for age_group in population:
    #     a,b = age_group
    #     csv_writer.writerow([age_group[0], age_group[1]])