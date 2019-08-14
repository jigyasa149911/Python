# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:11:06 2019

@author: jigyasa
"""

# LISTS IN PYTHON
l1=['abc',123,'d1c']
l2=[1,2,3,4,5]
l3=['Jigyasa','John','Mansi']
print(type(l1))  #type() returns type of the variable.
print(len(l3))   # len() returns length of the variable.

# INDEXING AND SLICING IN PYTHON
print(l1[:])       # ':' operator is called Range slice operator.
print(l1[0:])
print(l1[:5])
print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])
print(l2[4])
print(l3[0:2])
print(l3[2:3])
print(l3[-1])  # Negative indexing in python.
print(l3[:-1])

# OPERATORS IN LIST
print('1' in l2) # 'in' operator returns true if content between '' is present in the list.
print('Jigyasa' not in l3) #'not in' operator returns true if content between '' is present in list.

li1=['Jigyasa']
li2=['Chadhary']
li3=li1+li2        # '+' operator concatenates the list.
print(li3)

li3 = li1*2       # '*' operator repeats the strings.
print(li3)


# UPDATING LIST
l1=[1,2,3,4,5]
print(l1)
l1[1:4]=[34,22,33]
print(l1)

# ITEARTING A LIST
for i in l3:
    print(i)
    
# LIST FUNCTION
l1=['abc',123,'d2c']
l2=[1,2,3,4,5]
l3=['Rahul','John','Mansi']
l4=[98,65,87,98,23]
str='Jigyasa'

print(max(l2))  # max(list) returns maximum element of list.

print(min(l2)) # min(list) returns minimum element of list.

print(list(str)) # list(seq) Converts any sequence into list.

l1.append(432)  # list.append(obj) adds the element represented by obj to list.
print(l1)

l1.insert(2,'Jigyasa') #list.insert(index,obj) inserts the element represented by obj at index.
print(l1)

l1.reverse() # list.reverse() reverses the list.
print(l1)

l4.sort()  # list.sort() sortsbthe list.
print(l4)

l1.copy()  # prints a shallow copy of the list.
print(l1)

print(l1.count(432))  #list.count(obj) prints the number of occurence of the element represented by obj.

print(l1.index(432)) #list.count(obj) prints the index of element represented by obj when it's first encountered.

l1.extend([1,2,3])  # list.extend(seq) extends the list with sequence represented by seq.
print(l1)

l1.remove('Jigyasa') #list.remove(obj) removes the element represented by obj from list.
print(l1)

l1.pop()  # list.pop() removes the last element from the list.
print(l1)

l1.clear() # Removes all elements of list.
print(l1)









