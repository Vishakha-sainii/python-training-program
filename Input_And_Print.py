#Objective: Ask the user for their name and greet them.
#Task 1: Write a program that asks the user for their name and then prints a greeting   message using their name.

name = input('What is your name ? ')
print('Hello, ' , name)

#Objective: Perform basic arithmetic operations based on user input.
#Task 2: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.

num_1 = int(input('Please enter first number : '))
num_2 = int(input('Please enter second number : '))

print('Addition of these two numbers are : ' , num_1 + num_2)
print('Multiplication of these two numbers are : ' , num_1 * num_2)
print('Division of these two numbers are : ' , num_1 / num_2)

#Task 3: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names = input("Enter the names separated by commas : ")
names_list = names.split(',')
print(names_list)

#Task 4: Ask the user to enter their age and check if they are eligible to vote based on their age.

age = int(input('Please enter your age : '))
if age >= 18:
 print('You are eligible to vote')
else:
 print('You are not eligible to vote')

#Task 5: For value = 3.14159, Using f-string print output for only up to 2 decimal places.

value = 3.14159
print(f'{value:.2f}') 





