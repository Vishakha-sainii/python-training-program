#Given a list let's see how to double each element of the given list. Using map() 
#Expected Output: [2, 4, 6, 8]

a = [1, 2, 3, 4]
result = list(map(lambda x : x+x, a))
print("List After double each element : " , result)

#Use filter() and lambda to extract all even numbers from a list of integers.
#Expected Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x : x%2 == 0 , numbers))
print("Even Numbers : ", even_nums)


#Use reduce() and lambda to find the longest word in a list of strings.
#Expected Output: 'banana'

from functools import reduce
words = ["apple", "banana", "cherry", "date"]

longest_word = reduce(lambda acc, x: acc if len(acc) >= len(x) else x, words)
print("Longest Word : ", longest_word)

#Use map() to square each number in the list and round the result to one decimal place.
#Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squares = list(map(lambda x : round(x*x, 1),  my_floats))
print("Squares of Each Numbers in List: ", squares)

#Use filter() to select names with 7 or fewer characters from the list.
#Expected Output: ['olumide', 'josiah', 'omoseun']

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
result = list(filter(lambda x : len(x) <=7, my_names))
print(result)

#Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]

num_list = [1,2,3,4,5]
sum = reduce(lambda acc, x : acc + x , num_list)
print("Sum of all numbers in a list: ", sum)


#Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
#Expected Output : True

numbers = [1, 2, 3, 4, 5]
result = all(n > 0 for n in numbers)
print(result)

#Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
#Expected Output: True
numbers = [1, 3, 5, 7, 8]
result = any(n > 0 for n in numbers)
print(result)

#Determine if any number in a list is divisible by 5 an print.

num_list = [5,10,23,25,28,30]
result = any(n % 5 == 0 for n in num_list)
print(result)


#Using below list and enumerate(), print index followed by value. 
#Output: 0 apple
#1 banana
#2 cherry

fruits = ["apple", "banana", "cherry"]
for x, element in enumerate(fruits): 
 print(x, element)

#Using below dict and enumerate, print key followed by value
#Output:
#name: Alice
#age: 30
#city: New York

person = {"name": "Alice", "age": 30, "city": "New York"}
for x, (key, value) in enumerate(person.items()):
    print(f"{key}: {value}")


#Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
   
  #Output: [(2, 'banana'), (4, 'date')]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
result = [(i, fruit) for i, fruit in enumerate(fruits, start=1) if i % 2 == 0]
print(result)


#Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
minimum_value = min(numbers)
maximum_value = max(numbers)
print("Minimum Value : ", minimum_value)
print("Maximum Value: ", maximum_value)

#Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
minimum = min(setn)
maximum = max(setn)
print("Minimum Value : ", minimum)
print("Maximum Value: ", maximum)

#Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
#Output: ('kiwi', 'grapefruit')

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]

def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)
print(shortest_and_longest(words))

#Exception Handling
#Write a Python program that attempts to divide two numbers a = 10  b = 0
#and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error

a = 10
b = 0
try:
  print("diving a by b" , a/b)
except ZeroDivisionError as e:
   print(e)

#Apply exception handling to below code and handle an exception if the index is out of range. 
my_list = [1, 2, 3]
try:
 print(my_list[5])
except Exception as e:
   print(e)

#Correct this below code with appropriate exception handlings. And finally print “Execution completed”

def safe_divide(a,b):
      try:
       result = a / b
       print(f"Result: {result}")
      except ZeroDivisionError as e:
         print(e)
      except TypeError as e:
         print("Both inputs must be a number")
      finally:
         print("Execution Completed")
      
safe_divide(1,0)
safe_divide(1, "a")

#Decorators
#Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
import time
def time_calculator(func):
    def wrapper():
        start_time = time.time() #current timestamp in seconds
        func()
        end_time = time.time()
        print(f"Total time taken: {end_time - start_time} seconds")
    return wrapper


@time_calculator
def num_list():
   numbers = []
   for i in range(1, 1001):
      numbers.append(i)

num_list()

#Create a parameterised decorator retry that retries a function a specified number of times.
#@retry(3)
 #def may_fail(name):
#print(f"Hello, {name}!")

def retry(times):               
    def decorator(func):        
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
        return wrapper
    return decorator
    


@retry(3)
def may_fail(name):
   print(f"Hello, {name}")

may_fail("Vishakha Saini")


#Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.

def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            print("Error: Number must be positive")
            return
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
   return print("result", x ** 0.5)

square_root(3)

#Create a decorator cache that caches the result of a function based on its arguments.
def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result...")
            return print(cached_results[args])

        print("Performing computation1...")
        result = func(*args)
        cached_results[args] = result
        return print(result)

    return wrapper


@cache
def expensive_computation(x):
     print("Performing computation...")
     return x * x
	
expensive_computation(5)
expensive_computation(5)

#Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
def requires_permission(func):
  def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
  return wrapper
        


@requires_permission
def delete_user(user, user_id):
    		print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test’']}


delete_user(user1, 100)
delete_user(user2, 101)
delete_user(user3, 102)

#Generators
#Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers Of 10  numbers 

def fibonacci():
    a, b = 0, 1
    while True:          
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

#Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
#Input n=3

n = 3
def infinite_multiples(n):
    i = 1
    while True:          
        yield n * i
        i += 1
multiples = infinite_multiples(3)

for _ in range(5):
    print(next(multiples))

#Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.

word = "hello"
times = 5
def repeat_word(word, times):
    for _ in range(times):
        yield word
for w in repeat_word(word, times):
    print(w)


#File Handling
#Write a Python program to read the entire content of a file named sample.txt and display it.

with open("sample.txt", "r") as f:
    file_content = f.read()
    print(file_content)

#Write a Python program to count the number of words in a file named words.txt

with open("words.txt", "r") as f:
    file_content = f.read()
    word_count = len(file_content.split())
    print("Number of words in this file : ", word_count)



#Create a program to write the string “Hello, Python!” into a file named output.txt.

with open("output.txt", "w") as f:
    f.write("Hello, Python!")

# Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
#data = [["Name", "Roll Number", "Marks"],["Alice", "101", "85"],["Bob", "102", "90"],["Charlie", "103", "88"]]


import csv
with open("students.csv", "w") as f:
    data = [["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]]

    output_csv = csv.writer(f)     #output_csv = csv.writer(f, delimiter = '-')
    output_csv.writerows(data) 
    print("students csv created successfully")

#From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

def read_file(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line

for line in read_file("sample.txt"):
 print(line, end = "")


 #Modules : os, sys, datetime
import datetime

 #Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time

str_dt = "March 22, 2020 10:00 AM"
dt = datetime.datetime.strptime(str_dt, '%B %d, %Y %H:%M %p')
print("Original Date: ", dt)

dt_delta_days = datetime.timedelta(days=7)
dt_delta_time = datetime.timedelta(hours=12)

new_time = dt + dt_delta_days
new_updated_time = new_time + dt_delta_time
print("New time after adding a week and 12 hours: ", new_updated_time)


#Code to get the dates of yesterday, today, and tomorrow.
d_today = datetime.date.today()
d_delta = datetime.timedelta(days=1)

d_yesterday = d_today - d_delta
d_tomorrow = d_today + d_delta
print("Today's Date : ", d_today)
print("Yesterday's Date : ", d_yesterday)
print("Tomorrow's Date : ", d_tomorrow)


#Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
import os
print("Current Working Directory: ", os.getcwd())
os.makedirs("test")
for dirpaths, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpaths)
    print("Directories : ", dirnames)
    print("Files: ", filenames)

os.removedirs("test")

#Write a Python program to rename a file from old_name.txt to new_name.txt.

os.rename("old_name.txt", "new_name.txt")

#Create a file and Write a Python program to get the size of a file named example.txt
with open("example.txt", "w") as f:
    f.write("Python file")

print("Size of file: ",os.stat("example.txt").st_size)

#Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
#O/P: 2020-02-25 16:20:00

str_date = "Feb 25 2020 4:20PM" 
dt = datetime.datetime.strptime(str_date, '%b %d %Y %I:%M%p')
print(dt)

#Subtract 7 days from the date 2025-02-25 and print the result.
#O/P: New date: 2025-02-18
date = datetime.date(2025,2,25)
t_delta = datetime.timedelta(days=7)
new_date = date - t_delta
print("New Date after subtracting 7 days : ", new_date)

#Format the date 2020-02-25 as "Tuesday 25 February 2020"
t = datetime.date(2020,2,25)
formatted_date = dt.strftime('%A %d %B %Y')
print("Formatted Date : ",formatted_date)

#classes
#Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
  def __init__(self, name, age):
        self.name = name
        self.age = age
        
 
person = Person("Vishakha Saini", 23)  
print(person.name)
print(person.age)
 

#Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount(101, "Vishakha Saini", 5000)

account.check_balance()
account.deposit(1500)
account.withdraw(2000)
account.check_balance()


#Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#book = Book.from_string("Python Programming, John Doe")

class Book:
    def __init__(self, book_name, author_name):
        self.book_name = book_name
        self.author_name = author_name

    @classmethod
    def from_string(cls, book_string):
        book_name, author_name = book_string.split(", ")
        return cls(book_name, author_name)
    
book = Book.from_string("Python Programming, John Doe")

print(book.book_name)
print(book.author_name)

#Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#Write a code to perform multiple inheritance.

class Father:
    def father_method(self):
        print("This is father class method")

class Mother:
    def mother_method(self):
        print("This is mother class method")

class Child(Father, Mother):
    def child_method(self):
        print("This is child class method")    

c = Child()
c.father_method()
c.mother_method()
c.child_method()



