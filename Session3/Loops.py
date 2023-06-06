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

students = [
    ["Cindy","Emily","Eve"],
    ["Julie","Yara","Sargun"],
    ["Jenny","Sarah","Maddy"]
    ]
for student in students:
    print(student)
    for name in student:
        print(name)