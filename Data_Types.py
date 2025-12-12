#Task 1 : Task: Convert the following values to the specified types and print the results
#Convert 3.75 to an integer and print the value
num = int(3.75)
print('Integer Value is : ' , num )

#Convert "123" to a float and print the value
num = 123
num = float(num)
print('Float Value is : ' , num)

#Convert 0 to a boolean and print the value
num = bool(0)
print(num)

#Convert False to a string and print the value
str = str(False)
print(str)



#Task 2:
#Convert all characters in the string to uppercase. x = "hello"

x = 'hello'
print('String in uppercase : ', x.upper())


#Task 3 : Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.
x = 5
y = 3.14
z = x + y
print(type(z))
z = int(z)
print(type(z))



#Task 4 : Given the string s = 'hello', perform the following operations:
#Convert the string to uppercase.
s = 'hello'
print(s.upper())

#Replace 'e' with 'a'.
s = s.replace('e', 'a')
print('After Replacing e with a : ', s)

#Check if the string starts with 'he'.
print('String starts with he : ' , s.startswith('he'))

#Check if the string ends with 'lo'.
print('String ends with lo : ', s.endswith('lo'))





