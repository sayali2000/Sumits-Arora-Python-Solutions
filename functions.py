# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:00:43 2020

@author: Admin


dollars = float(input("Please enter dollars:"))
def dollar_to_rupees(dollars):
        print('$',dollars,'= Rs.',dollars*75) # approx dollar rate in pandemic

dollar_to_rupees(dollars) 



l,b,h=map(int,input("Enter length,breadth,height of a box:").split())
def volume_of_box(l=1,b=1,h=1):
    return l*b*h

print("Volume of box=",volume_of_box(l,b,h))



def find_cube(n=2):                 # (i)
    print('Cube of',n,'=', n**3)
def check_char_equal(c1,c2):        # (ii)
    return True if c1==c2 else False
find_cube()
find_cube(7)
print(check_char_equal('D','d'))
print(check_char_equal('D','D'))



import random
def gen_rand_nos(begin,end):
    return random.randint(begin,end)
begin,end=map(int,input("Enter Starting and Ending nos:").split())
print("Three random nos between",begin,'and',end,'are :',gen_rand_nos(begin,end),gen_rand_nos(begin,end),gen_rand_nos(begin,end))



def check_char_equal(s1,s2):        
    return True if len(s1)==len(s2) else False

print(check_char_equal('Welcome','Library'))
print(check_char_equal('Python','Fun'))


def nthRoot(x=2):       
    return x**(1/n)
x=int(input("Enter X value:"))   
n=int(input("Enter N value:"))       
print(1/n,'th root of',x,'=',nthRoot(x))

def function(f,l):
    return(f,int(f+(l-f)/3),int(f+2*(l-f)/3),l)
f=int(input("Enter First value:"))   
l=int(input("Enter Last value:"))       
print('Four equidistant terms between',f,'and',l,'are=',function(f,l))

def function(f,l):
    if f%10==l%10:
        return f,l  
    elif f%10<l%10:
        return f
    else: 
        return l
print(function(89,73))
print(function(82,72))
print(function(491,278))

"""
import random
def random_n_digits(n):
    min_v = 10 ** (n - 1)
    max_v = (10 ** n) - 1
    if n == 1:
        min_v = 0

    return random.randint(min_v, max_v)
n=int(input("Enter a value:"))  
print("Random numbers of",n,"digits is",random_n_digits(n))