#q1
name = input("Hello, what is your name?")

if not name:
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}! Good to meet you!")

#Q2

password1 = input("Enter a new password: ")

password2 = input("Confirm your password: ")

if password1 == password2:
    print("Password Set")
else:
    print("Error: Passwords do not match. Please try again.")

#q3

password1 = input("Enter a new password (8 to 12 characters): ")

password2 = input("Confirm your password: ")

if password1 == password2 and 8 <= len(password1) <= 12:
    print("Password Set")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters.")
else:
    print("Error: Passwords do not match. Please try again.")

#q4

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter a new password (8 to 12 characters): ")

password2 = input("Confirm your password: ")

if (
    password1 == password2
    and 8 <= len(password1) <= 12
    and password1 not in BAD_PASSWORDS
):
    print("Password Set")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters.")
elif password1 in BAD_PASSWORDS:
    print("Error: Common password. Please choose a more secure password.")
else:
    print("Error: Passwords do not match. Please try again.")

#q5

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8 to 12 characters): ")
    
    password2 = input("Confirm your password: ")

    if (
        password1 == password2
        and 8 <= len(password1) <= 12
        and password1 not in BAD_PASSWORDS
    ):
        print("Password Set")
        break
    elif len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters.")
    elif password1 in BAD_PASSWORDS:
        print("Error: Common password. Please choose a more secure password.")
    else:
        print("Error: Passwords do not match. Please try again.")
#q6
for i in range(13):
    result = i * 7
    print(f"{i} x 7 = {result}")
#q7
table_number = int(input("Enter the number for the times table (0 to 12): "))

if 0 <= table_number <= 12:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    print("Error: Please enter a number between 0 and 12.")

#q8
table_number = int(input("Enter the number for the times table (-12 to 12): "))

if -12 <= table_number <= 12:
    if table_number >= 0:
        for i in range(13):
            result = i * table_number
            print(f"{i} x {table_number} = {result}")
    else:
        for i in range(12, -1, -1):
            result = i * table_number
            print(f"{i} x {table_number} = {result}")
else:
    print("Error: Please enter a number between -12 and 12.")
