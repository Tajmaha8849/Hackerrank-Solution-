# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:30:25 2023

@author: shubh
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=set(arr)
    arr2=sorted(arr1)
    print(arr2[-2])
        
