# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:35:45 2020

@author: Admin
"""
"""
#Create a Input.txt file 
file=open('sports.dat','w')
for i in range(5):
    str1=input("Event:")
    str2=int(input("Participant:"))
    file.write(str1)
    file.write('~')
    file.write(str1+'\n')
    
file.close()



#Read complete Input file with read(),readline(),readlines()
# using read()
file=open('Input.txt','r')
str1=""
str1=file.read()
print(len(str1))
file.close()
# using readline()
file=open('Input.txt','r')
str1=str2=""
str1=file.readline()
while str1:
    str2+=str1
    str1=file.readline()
print(len(str2))
file.close()
file=open('Input.txt','r')
# using readlines()
str1=[]
str1=file.readlines()
print(len(str1))    
file.close()

file=open('Input.txt','r')
newfile=open('Output.txt','w')
str1=""
str1=file.read(1)
while str1:
    if str1==' ':
        str2=file.read(1)
        if str1==str2==' ':
            newfile.write(str1)
        else:
            newfile.write(str2)
    else:
        newfile.write(str1)
    str1=file.read(1)
file.close()
newfile.close()



f=open('Sports.dat','r')
# create list using readlines()
L=f.readlines()
nf=open('Athletics.dat','w')
for i in L:
    if 'Athletic' in i:
        nf.write(i)
f.close()
nf.close()
nf=open('Athletics.dat','r')
L=nf.read()
print(L)
nf.close()

#Create a Contacts.csv file 
file=open('Contacts.csv','w')
for i in range(5):
    str1=input("Name:")
    str2=int(input("Contact:"))
    file.write(str1)
    file.write('\t')
    file.write(str2+'\n')
   
import sys
f=open('Contacts.csv','r')
# create list using readlines()
L=f.readlines()  
print("Name \t Phone no") 
print("-"*20)
for i in L:
    v=i.split()
    '''sys.stdout.write(v[0]+' '+v[1]+'\n')   OR''' 
    print(v[0],' ',v[1])
file.close()

tocount=thecount=0
file=open('Input.txt','r')
L=file.readlines()
for i in L:
    if 'to' in i:
        tocount+=1
    if 'the' in i:
        thecount+=1
        
print("count of TO is",tocount,"count of THE is", thecount)   
file.close()


ucount=0
file=open('Input.txt','r')
str1=""
str1=file.read(1)
while str1:
    if str1.isupper():
        ucount+=1
    str1=file.read(1)
print("count of Upper Case letters is",ucount)   
file.close()

f1name=input("Enter First file\'s name:")
f2name=input("Enter Second file\'s name:")
f1=open(f1name,'r')
f2=open(f2name,'w')
L=f1.readlines()
for i in L:
    f2.write(i+'\n')
f1.close()
f2.close()


f1name=input("Enter First file\'s name:")
f2name=input("Enter Second file\'s name:")
f1=open(f1name,'r')
f2=open(f2name,'a')
L=f1.readlines()
for i in L:
    f2.write(i+'\n')
f1.close()
f2.close()



f1=open('Upper.txt','w')
f2=open('Lower.txt','w')
f3=open('Other.txt','w')
while True:
    c=input("Enter a character to wite in files OR Enter Exit to stop:")
    if c=='Exit':
        break
    elif c.isupper():
        f1.write(c)
    elif c.islower():
        f2.write(c)
    else :
        f3.write(c)
f1.close()
f2.close()
f3.close()


file=open('Input.txt','r')
# using readlines()
L=[]
count=0
L=file.readlines()
for i in L:
    if i[0]=='A':
        count+=1
print("Lines atarting with \'A\' are ", count)    
file.close()

"""
file=open('india map.jpg','r')
# using readlines()
'''L=[]
count=0
L=file.readline()
pos=file.tell()
print(pos)

L=file.readline()
pos=file.tell()
print(pos)

L=file.readline()
pos=file.tell()
print(pos)'''

file.seek(0)
L=file.read()
pos=file.tell()
print(L,pos)

