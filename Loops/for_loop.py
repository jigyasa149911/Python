# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:53:29 2019

@author: jigyasa
"""

''' Syntax of for loop:
    for iterating_var in sequence:
        statement(s)
        
    Syntax of nested for loop
    for iterating_var1 in seq:
        for iterating_var2 in seq:
            statement(s)
        statement(s)
'''

# Program to print 1-n.
i=1
n=int(input('Enter the range:'))
for i in range(1,n+1):
    print(i)
    

# Printing table of a guven number.
i=1
n=int(input('Enter the number:'))
for i in range(1,11):
    print('%d X %d = %d'%(n,i,n*i))


# Program to print sum of numbers.
i=1
s=0
n=int(input('Enter the number:'))
for i in range(1,n+1):
    s=s+i 
print('Sum is',s)

# Program to print fibonacci series.
i=1
a=0
b=1
n=int(input('Enter the number:'))
if(n<0):
    print('Incorrect input')
elif(n==0):
    print(a)
elif(n==1):
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
    
