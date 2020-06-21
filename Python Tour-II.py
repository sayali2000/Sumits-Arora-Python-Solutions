# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:17:06 2020

@author: Admin
"""
"""
ph = input('Enter Phone Number : ')
# length must be 12 and 3rd and 7th character should be '-'
if ((len(ph) == 12) and( ph[3] == '-') and (ph[7] == '-')):
    val = False
    if (ph[:3]+ph[4:7]+ph[8:]).isdigit(): # all the characters except dashes should be digits
        val = True
if val:
    print(ph, 'is valid')
else:
    print(ph, 'is invalid')
    
    
text = input('Enter a sentence : ')
wordscount = 1
charcount = len(text)
alnum = 0
for i in text:
    if i.isalnum():
        alnum += 1
    if i == ' ': # space indicates another word
        wordscount += 1
print('number of words ar', wordscount)
print('number of characters are', charcount)
print('percentage of characters that are alphanumeric is', int(alnum*100/len(text), '%')

L = list(map(int, input('Enter list of integers : ').split()))
M = list(map(int, input('Enter list of integers : ').split()))
if len(L) == len(M):
    N = [L[i]+M[i] for i in range(len(L))] 
print(N)

L = input("Enter elements:").split() # input().split() returns the list
L = L[len(L)-1:] + L[:-1] 
print(L)




L = input("Enter a sentence:").split() # input().split()
word,wlength='',0

for i in range(len(L)):
    if len(L[i])>wlength :
        word=L[i]
        wlength=len(L[i])
print("Longest word in the list is:",word,"of length",wlength)


L=[]
for i in range(1,101):
    if i%3==0 or i%5==0:
        L.append(i)
print("elements visible by 3 or 5 :",L)


first,second = 'Jimmy','Johny'
print("Before swap: first=",first,"second=",second) # Jimmy Johny
first, second = second, first # swaps the variables
print("After swap: first=",first,"second=",second) # Johny Jimmy


t1,t2=0,1
F=[t1,t2]
for i in range(2,9):
    t1,t2=t2,t2+t1
    F.append(t2)
print("Fibonacci Series upto nth Tearm:",tuple(F))

D={}
for i in range(12):
    m=input("Enter month name:")
    d=int(input("Enter no of days:"))
    D[m]=d
print(D)

m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
d=[31,28,31,30,31,30,31,31,30,31,30,31]
D={}
for i in range (len(m)):
    D[m[i]]=d[i]
print(D)

def addDict(dic1, dic2):
    '''new_dic = {}
    for i in dic1.keys(): # all the keys will be put into the new_dic
        new_dic[i] = dic1[i]

    for i in dic2.keys(): # keys common in both the dictionaries will have the values of dic2 in the new_dic
        new_dic[i] = dic2[i] 
    return new_dic'''
    return dict(list(dic1.items())+list(dic2.items()))

dic1 = {'a':11, 'b':12, 'c':13}
dic2 = {'c':14, 'd':5,'b':8,'a':19,'e':6}
print(addDict(dic1, dic2))
"""

dic1 = {'c':14, 'd':5,'b':8,'a':19,'e':6}
key=list(dic1.values())
print("keys before sort:",key)
for i in range(len(key)):
   for j in range(len(key)-1): 
       if(key[j]>key[j+1]):
           key[j],key[j+1]=key[j+1],key[j]
print("keys after sort:",key)
