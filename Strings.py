# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:50:12 2019

@author: jigyasa
"""

# Strings in Python

str='Hello World !'
print(type(str))    #type() returns type of the variable.
print(len(str))     # len() returns length of the variable.

# Indexing and slicing in strings.

print(str[:])       # ':' operator is called Range slice operator.
print(str[0:])
print(str[:5])
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[0:2])
print(str[1:3])
print(str[-1])  # Negative indexing in python.
print(str[:-1])

# String operators.
print('e' in str) # 'in' operator returns true if content between '' is present in the string.
print('p' not in str) #'not in' operator returns true if content between '' is present in string.

str1= 'Hello'
str2 = 'World'
str3 = str1+str2   # '+' operator concatenates the strings.
print(str3)

s4 = str1*2       # '*' operator repeats the strings.
print(s4)

print('%s I am Jigyasa'%(str1))  # '%' operator is format specifier.
print('%s\t%s'%(str1,str2))
print('Hey',str1)


# String Functions.
str='Jigyasa'
s1='abc'
s2='12345'

print(str.lower())  # str.lower() tranforms string into lowercase.

print(str.upper()) # str.upper() transforms string into uppercase.

print(str.title()) # str.title() in a form where first letter is uppercase and rest in lowercase.

print(s1.capitalize()) # str.capitalize() tranforms first letter of string in uppercase.

print(str.count('a'))  # str.count('eg') returns the no. of occurence of elemnet between ''.

print(str.isupper())  # str.isupper() returns true if string is in uppercase.

print(str.islower())  # str.islower() returns true if string is in lowercase.

print(str.istitle())  # str.istitle() returns true if string is in titlecase.

print(str.index('a')) #str.index('eg') returns index of the item when it is first encountered.

print(str.isalnum()) # str.isalnum() returns true if string is in alphanumeric case.

print(str.isnumeric()) #str.isnumeric() returns true if string is in numeric case.

print(s2.isdecimal()) #str.isdecimal() returns true if all character of string is decimal.

print(s2.isdigit()) #str.isdigit() returns true if all character of string are digit.

print(s4.isspace()) #str.isspace() returns true if there is whitespace in string.








