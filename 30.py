# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:25:35 2024

@author: ASUS
"""
a = int ( input ("Nhập năm: ") )
b = int ( input ("Nhập tháng: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print ("Đó là năm nhuận")
    if b == 2:
        print ("Tháng đó có 29 ngày")
else:
    print ("Đó không phải là năm nhuận")
    if b == 2:
        print ("Tháng đó có 28 ngày")
if b in [1,3,5,7,8,10,12]:
    print ("Tháng đó có 31 ngày")
if b in [4,6,9,11]:
    print ("Tháng đó có 30 ngày")