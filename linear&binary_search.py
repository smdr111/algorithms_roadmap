#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:26:25 2025

@author: samandaroripov
"""

def linear(mylist,x):
    for y in range(len(mylist)):
        if mylist[y]==x:
            return y
    return -1
        
mylist = [1,3,4,6,7,8,10,12,23,45,56,78,99]

print(linear(mylist,6))


def binary(mylist,x):
    b=len(mylist)-1
    a=0
    while a<=b:
        m=(a+b)//2
        if mylist[m]==x:
            return m
        elif mylist[m]<x:
            a=m+1
        else:
            b=m-1
    return -1
        
print(binary(mylist,8))



