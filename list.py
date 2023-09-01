# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:33:28 2023

@author: shubh
"""

lst=[]
n=int(input())
for i in range(n):
    command=input().split();
    if command[0] == "insert":
        lst.insert(int(command[1]),int(command[2]))

    elif command[0] == "append":

        lst.append(int(command[1]))

    elif command[0] == "pop":

        lst.pop();

    elif command[0] == "print":

        print(lst)

    elif command[0] == "remove":

        lst.remove(int(command[1]))

    elif command[0] == "sort":

        lst.sort();

    else:

        lst.reverse();
