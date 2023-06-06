# # Boolean
# # Mathematical operators
# # Boolean Expressions - And, Or, Nort
# name = "NJ"
# age = 31
# height = 152
# is_raining = False

# # Boolean Expression 
# # we can compare booleN DATATYPES and get the answer
# # = is equal
# # != not equal 
# # > greater than 
# # < less than
# # >= greater than equal to
# # <= Less than equal to


# # is_sunny = True
# # is_cold = True

# # print(is_sunny and is_cold)

# # Temprature = 17

# # if Temprature < 18:
# #     print("the weather is nice!")
# # elif Temprature > 28:
# #     print("It is burning outside")
# # else: 
# #     print("stay in your bed")

# # sara_has_helmet = True
# # sara_has_helmet = False

# # if sara_has_helmet == True:
# #     print("go for the hike")
# # else:
# #     print("NO WAY, my brain is my monneymaker")

# # sara_has_helmet = False
# # rei_has_rope = False

# # if sara_has_helmet != rei_has_rope:
# #     print("Let's send it")

# # elif sara_has_helmet  and rei_has_rope:
# #     print("No way, my brain is my moneymaker")

# # elif rei_has_rope or sara_has_helmet:
# #     print("who is unprepared now, Rei?")

# # else:
# #     print("I guess let's just go hiking?")

# # light_color = "Amber"
# # car_detected = True

# # if car_detected == light_color:
# #     print("do nothing")
# # else:
# #     print("Flash")

# # height = int(input("Please add youe height "))

# # if height >= 120:
# #     print("Hop on!")
# # else:
# #     print("Hop on")

# email = str(input("Please add you email "))

# if email == "lucyg" or email == "quartzgleam?1":
#     print("Logged in successfully")
# else:
#     print("Acess denied")

# # # string, integer, float, list
# # # list_name = ["Nj", 1 2 3 4, []] 

# # if "True":
# #     print("A strange game. The only winning move is not to play.")
# # else:
# #     print("you are dumb")
    

# # digit.pop()

# # letter = ['a', 'b,', 'c', 'd', ['claire', 'NJ', 'joy', 'Ashley']]
# # print(letter[4][0])

# # if 'A' in letter:
# #     print("it is in the list")


# Q1
# Given the list of foods below, print:
# The first item in the list.
# The third item in the list.
# The last item in the list.The first three items in the list.
# The last three items in the list.The last item in the sublist.

foods = ["orange","apple","banana","strawberry","grape","blueberry", ["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
print(foods[0])
print(foods[2])
print(foods[9])
print(foods[0:3])
print(foods[7:11])
print(foods[6][-1])


# Q2
# Format and print the contents of the following list so that the output appears asdepicted:

data = [
    ["Monica", "in my life"],
    ["Erica", "by my side"],
    ["Rita's", "all I need"],
    ["Tina's", "what I see"],
    ["Sandra", "in the sun"],
    ["Mary", "having fun"],
    ["Jessica", "here I am"]
]

output = ""
for item in data:
    output += f"A little bit of {item[0]} {item[1]};\n"

output += "A little bit of you makes me your man (ah!)*trumpet solo*"

print(output)


# Q3
# Ask the user for three names. Add each name to a list, and then print the list
# I have used 2 approaches

# Approach 1
# Ask the user for three names

name_list = []
for i in range(3):
    name = input("Enter a name: ")
    name_list.append(name)

# Print the list
for name in name_list:
    print(name)

# Approach 2
# Ask the user for three names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")

# Add names to a list
name_list = [name1, name2, name3]

# Print the list
print(name_list)


# Q4
# Using the following starter code

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

print(a, b, c)

d = a + b + c

print(d)