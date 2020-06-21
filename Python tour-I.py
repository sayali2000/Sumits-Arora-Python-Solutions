# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:37:32 2020

@author: Admin
"""
"""
x=int(input("Enter a number"))
if(x<0):
    print("-Ve")
elif (x==0):
    print("Zero")
else:
    print("+ve")


   
x=int(input("Enter a number"))
if(x%2==0):
    print("Even")
else:
    print("Odd")
   

days,hours,minutes,seconds=365,24,60,60
print("Number of Seconds in a year= ", days*hours*minutes*seconds)
    
   
x,y=map(int,input("Enter two numbers:").split())
if(x%y==0):
    print("First number is divisible by Second")
else:
    print("First number is not divisible by Second")
  

x = int(input('Enter day number between 2 & 365 : '))
d = input('Enter first day of the year (Sunday/Monday/Tuesday....) : ')
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
print(days[(x%7)-1 + days.index(d)  ]) 


def feet_to_inches(x):
    return x*12

def Input():
    return int(input('Enter length in feet = '))

def display_inches(x):
    print('Number of inches =', x)
    
x= Input()
x = feet_to_inches(x)
display_inches(x)


n = int(input('Enter a Number:'))
sum = 0
if n < 0:
    for i in range(2*n, n+1): 
        sum += i
    print("Sum of numbers from ",n,"to",2*n,"=",sum) 
else:
    for i in range(n, 2*n+1):
        sum += i
    print("Sum of numbers from ",n,"to",2*n,"=",sum) 

date=input("Enter a date in MMDDYYYY format:")
months=['January','February','March','April','May','June','July','August','September','October','November','December']
MM=months[int(date[:2])-1]
DD=date[2:4]
YYYY=date[4:]
print(MM, DD,',',YYYY)



print('Miles','\t | \t',' Km  ')
print('-'*25)
for i in range(1,106,5):
    #print(i,' mi ','\t|\t',i*1.609,'Km ') #it wont print appropriate table
    print('{} mi\t | \t {} km'.format(i,i*1.609)) # it  will help to print perfect table



print('Pounds','\t | \t',' Kg  ')
print('-'*25)
for i in range(1,101,10):
    #print(i,' mi ','\t|\t',i*1.609,'Km ') #it wont print appropriate table
    print('{} lb\t | \t {} kg'.format(i,i*0.453))     
    (int(x[2:]))-(int(y[2:]))
    """
x=input("Enter First Time in military format :")
y=input("Enter Second Time in military format :")
h=int(y[:2])-int(x[:2])
m=int(y[2:])-int(x[2:])
print (h,'hours',m,'minutes')

