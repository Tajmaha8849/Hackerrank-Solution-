# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:39:44 2023

@author: shubh
"""

def mutate_string(string, position, character):
    x=list(string)
    x[position]=character
    str=""
    for i in range(len(x)):
        str=str+x[i]   
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)