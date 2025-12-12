#Task1 : Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.
 
def calculate_area(length , width = 10):
  print("Area of Rectangle is : " , length * width)
length = int(input("Enter the length: "))
width = input("Enter the width: ")
if width == "":
  calculate_area(length) #width will be 10 byDefault
else:
 calculate_area(length, int(width))
 
#Task2 : Write a recursive function to compute the factorial of a non-negative integer.

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
    
#Task 3: Write a function that takes one parameter as a string and reverse it and return.

def reverse_string(s):
  reversed_str = ""
  for char in s:
        reversed_str = char + reversed_str
  return reversed_str
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))

#Task 4 : Write a Python function that takes two parameters as lists and to sum all the numbers in a list. a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.

def sum_two_lists(list1, list2):
    return sum(list1) + sum(list2)
a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
result = sum_two_lists(a, b)
print("Total Sum =", result)

#Task 5: Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7] , Output = [1,2,3,4,5,7]
def distinct_sorted(numbers):
    return sorted(set(numbers))
a = [4,1,2,3,3,1,3,4,5,1,7]
result = distinct_sorted(a)
print(result)

 
  

