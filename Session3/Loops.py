# letters = ['a', 'b', 'c',]
# print(letters[0])
# print(letters[1])
# print(letters[2])


# Loops are used for repitive tasks
# there are 2 types of Loops
# FOR and WHILE

# Learning the While Loop

# count = 0
# while 5 > count:
#     print("Hello")
#     count = count + 1

# name = input("what is your name?")
# while name != "Ashley":
#     print("I dont know you")
#     name = input("well, what's your name")

# Learning the FOR loop

# letters = ["a", "b", "c", "d"]

# for items in letters: # item here is sort of index of list 
#     print(items)

# for number in range(10):
#     print(number)

# students = [
#     ["Cindy","Emily","Eve"],
#     ["Julie","Yara","Sargun"],
#     ["Jenny","Sarah","Maddy"]
#     ]
# for student in students:
#     print(student)
#     for name in student:
#         print(name)

<<<<<<< HEAD
# count = 0
# while 5 > count:
#     print(f"Hello, the number is {count}")
#     count += 1


                            # Exercise #
# Q1 Continuously ask the user to enter a number until they provide a blank input. Outputthe sum of all the numbers.

count = 0
num1 = input("Please enter a number")
while num1 != '':
   count = count + int(num1)
   num1 = input("Please enter a number")
print(count)

# Q2
# Ask the user to enter a in integer number. Print all the odd numbers between 0 andthat number (inclusive).

number = int(input("Please enter a number"))

digit = 0
while digit <= number:
   if digit % 2 != 0:
      print(digit)
   digit += 1
=======
# # count = 0
# # while 5 > count:
# #     print(f"Hello, the number is {count}")
# #     count += 1


#                             # Exercise #
# # Q1 Continuously ask the user to enter a number until they provide a blank input. Outputthe sum of all the numbers.

# count = 0
# num1 = input("Please enter a number")
# while num1 != '':
#    count = count + int(num1)
#    num1 = input("Please enter a number")
# print(count)

# # Q2
# # Ask the user to enter a in integer number. Print all the odd numbers between 0 andthat number (inclusive).

# number = int(input("Please enter a number"))

# digit = 0
# while digit <= number:
#    if digit % 2 != 0:
#       print(digit)
#    digit += 1
>>>>>>> d2e4e10 (Initial commit)

# Q3 Write a guessing game.
# Select a number, and save it as a variable in your code. 
# Ask the user to enter anumber, and then output whether their number is less than or greater than theselected number. 
# Keep asking until the user guesses the correct number. Then print acongratulatatory message.


<<<<<<< HEAD
print("Welcome to the Guessing Game")

number = int(input("Please enter a number "))

lucky_number = 7

while number >= 0:
   if number < 100 and number != lucky_number:
      print("Oh Ho! you missed it, try again")
      number = int(input("Please enter the number again "))
   if number == lucky_number:
      print("You Nailed it ")
      break



=======
# print("Welcome to the Guessing Game")

# number = int(input("Please enter a number "))

# lucky_number = 7

# while number >= 0:
#    if number < 100 and number != lucky_number:
#       print("Oh Ho! you missed it, try again")
#       number = int(input("Please enter the number again "))
#    elif number == lucky_number:
#       print("You Nailed it ")
#       break



# print("Welcome to the Guessing Game")

# number = int(input("Please enter a number "))

# lucky_number = 7

# while number != lucky_number:
#    if number < lucky_number:
#       print("Oh Ho! It is too low, try again")
#    elif number > lucky_number:
#       print("Oh Ho! It is too High, Try Again")
#    else:
#       print("Horray! you nailed it")
#       break
#    number = int(input("Please enter the number again "))



   # For Loop

# Q2 Ask the user for an integer. Using a for loop, add up every number from 0 up to that integer, and print the result

user_input = int(input("Please enter a number"))
count_number = 0

for num in range(0, user_input + 1):
   count_number +=  num
   print(count_number)

>>>>>>> d2e4e10 (Initial commit)
