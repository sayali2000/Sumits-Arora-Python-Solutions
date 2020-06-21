# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:06:00 2020

@author: Admin
"""
"""
# pg 332 Type C Q1
def find_in_list(lst,v):
    c=-1
    for i in range(len(lst)):
        if lst[i]==v:
            return i
    else:
            return -1
L=eval(input("Enter list elements:"))
V=int(input("Enter element to find in list:"))
ans=find_in_list(L,V)
if ans==-1:
    print(V,"not found")
else:
    print(V,"found at position",ans+1)
    
Output-
Enter list elements:[45,32,34,90]

Enter element to find in list:90
90 found at position 4

Enter list elements:[45,32,34,90]

Enter element to find in list:10
10 not found

# pg 332 Type C Q2
def unique(lst):
    if lst==[]:
        return -1
    else:
        T=[]
        for i in lst:
            if i not in  T:
                T.append(i)
    return len(T)
lst=[]
print(unique(lst))  # as lst is empty it reurn -1
lst=[1,2,3]
print(unique(lst))  # as lst has all unique elements, returns 3
lst=[1,2,2]
print(unique(lst))  # as lst has two unique elements, returns 2
lst=[1,2,2,3,3]
print(unique(lst)) # as lst has 3 unique elements, returns 3

Output-
-1
3
2
3


# pg 332 Type C Q3

CB4=[i**3 for i in range(1,11) if i**3 %4==0]
print(CB4)

Output-
[8, 64, 216, 512, 1000]
"""


# pg 332 Type C Q4
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
x=[set([i for i in a if i in b])]
print(x)
Output-
[{1, 2, 3, 5, 8, 13}]

"""
# pg 332 Type C Q5
def MVisit(Lst):
    max=len(Lst[0])
    pos=0
    for i in range(1,len(Lst)):
        if len(Lst[i])>max:
            max=len(Lst[i])
            pos=i
    return Lst[pos]
p=int(input("Enter no of patients:"))
V=[]
for i in range(p):
    dd=[]
    dd=eval(input("enter visited days for patient "+str(i+1)+":"))
    V.append(dd)
print("Total patients=>",p,"Highest no of visites by patient=> ",MVisit(V))

Output-
Enter no of patients:6

enter visited days for patient 1:[2,6]

enter visited days for patient 2:[3,10]

enter visited days for patient 3:[15]

enter visited days for patient 4:[23]

enter visited days for patient 5:[1,8,15,22,29]

enter visited days for patient 6:[14]

Total patients=> 6 
Highest no of visites by patient=>  [1, 8, 15, 22, 29]

"""
