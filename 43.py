# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:20:40 2024

@author: ASUS
"""
n = int ( input ("Nhập số nguyên dương chẵn n: "))
while n <= 0:
    n = int ( input ("Nhập lại số nguyên dương chẵn n: "))
s = 0
for i in range (1,n+1):
    s += i/(i+1)
print ("S = ",s)
