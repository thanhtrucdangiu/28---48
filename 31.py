# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:38:29 2024

@author: ASUS
"""
a = int ( input ("Nhập số nguyên dương a: "))
b = int ( input ("Nhập số nguyên dương b: "))
c = int ( input ("Nhập số nguyên dương c: "))
if a + b > c or a + c > b or c + b > a:
    if a == b == c:
        print ("Đây là tam giác đều")
    elif a == b != c or a == c != b or b == c != a:
        print ("Đây là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print ("Đây là tam giác vuông")
    else:
        print ("Đây là tam giác thường")
else:
    print ("Ba số trên không tạo thành một tam giác")
