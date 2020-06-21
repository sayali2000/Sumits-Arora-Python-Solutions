# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:13:41 2020

@author: Admin
"""

file=open('.\Files\SubFiles\InAdmin.txt','r') # InAdmin is inside # using readlines()
L=[]
count=0
L=file.readline()
pos=file.tell()
print(pos)
