#Q1
name=str(input("hello, what is your name?"))
print(f"Hello, {name} Good to meet you!")

#Q2
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}C is equivalent to {fahrenheit}F.")

#Q3
num_students = int(input("How many students? "))
group_size = int(input("Required group size? "))
num_groups = num_students // group_size
students_left_over = num_students % group_size
print(f"There will be {num_groups} groups with {students_left_over} students left over.")

#q4
total_sweets = int(input("total number of sweets: "))
num_pupils = int(input("number of pupils: "))
sweets_per_pupil = total_sweets // num_pupils
sweets_left_over = total_sweets % num_pupils

print(f"Each pupil will receive {sweets_per_pupil} sweets, with {sweets_left_over} sweets left over.")
