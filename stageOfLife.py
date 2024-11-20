import math
name = input("What is your name?: ")
print("hello " + str(name))

age = input("What is your age?: ")

if age >= 8 and age <= 12:
    print("You are currently in the Childhood stage of your life. ")
elif age >= 13 and age <= 19:
    print("You are currently in the Teenager stage of your life. ")
elif age >= 20 and age <= 29:
    print("You are currently in the Young Adult stage of your life. ")
elif age >= 30 and age <= 55:
    print("You are currently in the Adult stage of your life. ")
elif age >= 56 and age <= 65:
    print("You are currently in the Wise Person stage of your life. ")
elif age >= 66 and age <= 100:
    print("You are currently in the Retirement stage of your life. ")
