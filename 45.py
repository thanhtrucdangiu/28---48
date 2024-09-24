# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:32:33 2024

@author: ASUS
"""
n = int ( input ("Nhập n: "))
x = float ( input ("Nhập x: "))
while n <= 0:
    n = int ( input ("Nhập lại n: "))
s1 = 0
s2 = 0
for i in range (1,n+1):
    s1 = s1 + i
    s2 = s2 + x**i/s1
print ("S = ",s2)
