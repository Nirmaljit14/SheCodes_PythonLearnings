# Function - An activity that is natural to or the purpose of a person or thing
# Functions we've already have are -
# input(), len(), int(), print()

# Task Separation

# def ask_userName():
#     name = input("What is your name? ")
#     return name

# print("Hello")
# answer = ask_userName()
# print(answer)

# def ask_userAge():
#     age = int(input("Please enter your age?"))
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("You are underage")

# Funciton definition


# Parameters
# def add (num1, num2):
#     result = num1 + num2
#     return result

# answer = add(2,3)
# print(answer)

# Q1 Write a function called get_integer that takes a string as its argument, 
# and uses thatstring to prompt the user to enter an integer. 
# Your function should return the integersupplied by the user

def get_integer(prompt):
    print(f"your integer is {prompt}? Thanks!")
    return prompt

user_input = input("Please enter an integer")
result = get_integer(user_input)

# Q2 Write a function called celcius_convert that takes a number representing thetemperature in Farenheit 
# as its argument, and returns a float representing thetemperature in Celcius.

degree_f = 32
def celcius_convert(temp_f):
    temp_f = degree_f * 9/5 + 32
    return temp_f

user_input = float(input("Please emter the temprature "))
results = celcius_convert(user_input)
print(results)


# Q3Write a function that accepts one argument (an integer) and returns True when that 
# argument is odd and False when that argument is even. 
# You can use the same formatas the starter code in the previous exercise. 
# Just remember - you're returning theresult, not printing it!

def numCheck(number):
    if number % 2 == 0:
        print("True")
    else:
        print("False")
    return number

digit = int(input("Please enter a digit for numCheck "))
results = numCheck(digit)
print(results)

# Q4 Write a function that takes two arguments; the unit price of an item, 
# and how manyunits were purchased. 
# Return the total cost as a string.

def price_calculator():
    unit_price = float(input("Please enter the price "))
    num_units = float(input("please enter the number of units you wish to buy "))
    total = unit_price * num_units
    print(total)


print("Please scan the bar code on the item")
total_owing = price_calculator()
    