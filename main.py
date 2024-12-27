# Program to check if the entered age is between 10 to 20 years
age = int(input("Enter your age: "))

if age >= 10:  # Outer condition
    if age <= 20:  # Nested condition
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is greater than 20.")
else:
    print("Your age is less than 10.")
