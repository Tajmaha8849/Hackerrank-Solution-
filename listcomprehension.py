# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:29:30 2023

@author: shubh
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))
    
