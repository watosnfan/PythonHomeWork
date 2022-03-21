# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:20:33 2022

@author: USER
"""


result = 0

while True:
    num = int(input("請輸入數字加總，-1離開:"))
    if num == -1:
        break
    result += num
    
print("加總和：",result)    