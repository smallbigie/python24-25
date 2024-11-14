print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero

# Write an if/else (elif) structure to determine the number's positive, negative, zero state

number = int(input("Please enter a number: "))

if number > 0:
    print("The number is Positive")
elif number == 0:
    print("The number is Zero State")
elif number < 0:
    print("The number is Negative")




print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = "admin"

# Write your Code Below

password = input("Enter admin password: ") #"password123"

if password == "password123":
    print("You have admin Privilages ")
else:
    print("You do not have permission to admin Privilages")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
year = 2024

# Write your Code Below

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This year is a Leap year")
else:
    print("This year is not a Leap year")



print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = 25

# Write your Code Below

if age < 13:
    print("Your age group is Kid")
elif age >= 13 and age <= 18:
    print("Your age group is Teenager")
elif age > 18 and age < 30:
    print("Your age group is Young Adult")
elif age >= 30 and age < 50:
    print("Your age group is Middle Aged")
elif age >= 50:
    print("Older person")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = 120

# Write your code Below

if purchase_amount > 30:
    print("You get a 5% Discount")
elif purchase_amount > 60:
    print("You get a 10% Discount")
elif purchase_amount > 100:
    print("You get a 15% Discount")
elif purchase_amount >= 200:
    print("You get a 20% Discount")