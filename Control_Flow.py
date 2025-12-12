#For loop
#Task 1 : Write a program that takes the input from the user and checks if a number is even or odd.
nums = input("Enter numbers separated by commas: ")
# convert input into list of integers
num_list = [int(n) for n in nums.split(',')]
for num in num_list:
    if num % 2 == 0:
        print(num, "is Even Number")
    else:
        print(num, "is Odd Number")
        
#Task 2 : Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
word = input("Enter a word: ")
reversed_word = ""
# Reverse using for loop
for ch in word:
    reversed_word = ch + reversed_word
print("Reversed:", reversed_word)
# Check palindrome
if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    
#Task 3 : Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
numbers = int(input("Enter, How many fibonacci numbers you want : "))
a = 0
b = 1
for n in range(numbers):
    print(a)
    temp = a
    a = b
    b = temp + b
    
#Task 4 : From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]
nums = [1,2,3,4,5]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            print([nums[i], nums[j]])

#For loop
#Task 5 :Print all even numbers between 1 and 20 using a while loop.
num = 1
while num < 20:
 if num % 2 == 0:
  print(num)
 num += 1
print("These are all even numbers between 1 and 20") 

#Break
#Task 6 : Find the first occurrence of a number in a list and stop further searching. 
numbers = [10, 20, 30, 40, 50]
search_for = 30
for n in numbers:
 if n == search_for:
   print("Found : ", n)
   break
   
#Continue
#Task 7 : Using continue statement, print only the odd numbers from 1 to 10.
num = 1
while num <= 10:
 if num % 2 == 0:
   num += 1
   continue
 print(num)
 num += 1
 
#Pass
#Task 8: What will be the output 
for i in range(5):
    if i == 3:
        pass  
    print(i)

#Match
#Task 9: Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
user_day = input("Enter a day : " )
def is_weekend(user_day):
 match user_day:
   case  "Sunday" | "Saturday":
    return "Its Weekend !"
   case  "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
     return "Its a Weekday !"
   case _:
     return "Not a valid day"  
print(is_weekend(user_day))  

   

 

  
  





 





