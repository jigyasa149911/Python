# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:10:52 2019

@author: jigyasa
"""

'''Syntax of if statement:
    if expression:
        statement(s)
  -----------------------------     
    Syntax of if-else
    if exp:
        statement(s)
    else:
        statement(s)
   ----------------------------     
    Syntax of elif statement
    if ex1:
        statements
    elif ex2:
        statement(s)
    elif ex3:
        statement(S)
    else:
        statement(s)
'''

# Program to check whether a number is even.
num=int(input('Enter the number:'))
if num%2==0:
    print('%d is Even'%(num))

# Program to check which number is greater.
num=int(input('Enter 1st number:'))
num1=int(input('Enter 2nd number:'))
if num>num1:
    print('%d is greater than %d'%(num,num1))
else:
    print('%d is greater than %d'%(num1,num))
    
# Program to check grade of a student using percentage.
marks=int(input('Enter the percentage:'))
if marks>85 and marks<=100:
    print('Congrats! Grade A')
elif marks>60 and marks<=85:
    print('Grade B')
elif marks>40 and marks<=60:
    print('Grade C')
elif marks>30 and marks<=40:
    print('Grade D')
else:
    print('Fail!')

