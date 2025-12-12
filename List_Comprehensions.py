#Task 1 : Given a list of numeric strings, convert them into integers. Using List Comprehensions
strings = ["1", "2", "3", "4", "5"]
#Expected output : [1, 2, 3, 4, 5]
numbers = [int(s) for s in strings]
print(numbers)

#Task 2 : Extract all integers from a list that are greater than 10. Using List Comprehensions
numbers = [1, 5, 13, 4, 16, 7]
#Expected output :[13, 16]
result = [n for n in numbers if n > 10]
print(result)

#Task 3 : Create a list of squares for numbers from 1 to 5. Using List Comprehensions
#Expected output :[1, 4, 9, 16, 25]

squares = [n*n for n in range(1, 6)]
print(squares)

#Task 4 : Convert a 2D list into a 1D list.Using List Comprehensions
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
#Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]
result_matrix = [num for row in matrix for num in row]
print(result_matrix)

#Task 5 : Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
#Expected output : {'a': 1, 'b': 2, 'c': 3}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {keys[i]: values[i] for i in range(len(keys))}
print(result)

#Task 6 : Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
	#Expected output : {'Alice': 85, 'Charlie': 90}
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
filtered_scores = {name: score for name, score in scores.items() if score > 80}
print(filtered_scores)



 
