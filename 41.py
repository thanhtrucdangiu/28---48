# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:18:19 2024

@author: ASUS
"""
n = int ( input ("Nhập số nguyên dương n: "))
while n <= 0:
    n = int ( input ("Nhập lại số nguyên dương n: "))
s = 0
for i in range (0,n+1):
    s += 1/(2*i+1)
print ("S = ",s)
