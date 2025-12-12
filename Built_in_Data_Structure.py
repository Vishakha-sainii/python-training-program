# 1. Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
print('Maximum Number : ', max(nums))
print('Minimum Number : ', min(nums))

#2. Given two lists below, merge the values from both lists to one and print
a = [1,2,3,4]   
b = [5,6,7,8] 
merged_list = a + b
print('Merged List : ' , merged_list)

#3. From a list, print the number of times the value 3 appears in the list:
a = [1,3,4,5,2,1,3,9,3]
print(a.count(3))

#4. From below list, Sort the list and print
a = [1,3,4,5,2,1,3,9,3]
a.sort()
print('Sorted List : ', a)

#5. Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print('Updated set after adding 6 : ' , numbers)

#6. Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print('Updated set after removing 3 : ' , numbers)
		
#7. Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('Intersection of these two sets : ' , set1.intersection(set2))
				
#8. Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
print(fruits.count('apple'))
		
#9. Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6)
concatenated_result = tuple1 + tuple2
print('After concatenation : ' , concatenated_result)

#10. Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
print('Value associated with age :' , person.get('age'))
		
#11. Add new key,  gender to dictionary and assign “M” to it and print
person = {"name": "Alice", "age": 30, "city": "New York"}
person['gender'] = 'M'
print('After adding gender:', person)

#12.Remove the key "city" from the above Dict and print
del person['city']
print('After removing city :', person)

#13. Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print('After merging the dictionaries : ', merged_dict)









