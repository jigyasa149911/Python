# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:16:04 2019

@author: jigyasa
"""

''' Syntax of while loop
    while expression:
        statement(s)
'''

# Program to print 1-n numbers.
i=1
n=int(input('Enter the number:'))
while i<=n:
    print(i)
    i=i+1


# Program to print table of a number.
i=1
n=int(input('Enter the number:'))
while i<=10:
    print('%d X %d = %d'%(n,i,n*i))
    i=i+1


# Program to print the entered number.
i=1
while i!=2:
    n=int(input('Enter the number:'))
    print('Entered value is %d'%(n))
    i=i+1
else:
    print('End of statement')

