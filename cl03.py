# Create a program that asks the user to enter their name and their age. Print out a
# message addressed to them that tells them the year that they will turn 100 years old


name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2026

year = current_year + (100 - age)

print(f"{name}, you will turn 100 years old in the year {year}.")




























