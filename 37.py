# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:26:01 2024

@author: ASUS
"""
n = int ( input ("Nhập số nguyên dương chẵn n: "))
while n <= 0:
    n = int ( input ("Nhập lại số nguyên dương chẵn n: "))
s = 0
for i in range (2,n+1,2):
    s += i
print ("S = ",s)

