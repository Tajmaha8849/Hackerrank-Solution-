# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:37:01 2023

@author: shubh
"""

def swap_case(s):
    string=" "
    for ch in s:
        if(ch.islower()):
            string=string+ch.upper()
        else:
            string=string+ch.lower()
        
            
    return string.strip()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)