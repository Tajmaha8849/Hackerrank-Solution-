# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:19:37 2023

@author: shubh
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n>=1 and n<=100):
        if(n>=2 and n<=5):
            if(n%2==0):
                print("Not Weird")
            else:
                print("Weird")
                
        if(n>=6 and n<=20):
            if(n%2==0):
                print("Weird")
            else:
                print("Not Weird")
        if(n>20):
            if(n%2==0):
                print("Not Weird")
            else:
                print("Weird")
