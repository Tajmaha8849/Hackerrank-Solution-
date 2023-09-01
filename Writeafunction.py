# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:26:25 2023

@author: shubh
"""

def is_leap(year):
    if(year>=1900 and year<=10**5):
        if(year%4==0 ):
            if(year%100==0 and year%400==0):
                return True
            elif year%4==0 and year%100!=0:
                return True
                                    
            else:
                return False
                
            
            
        else:
            return False
    else:
        return False 
            
    
    
    # Write your logic here
    
    

year = int(input())
print(is_leap(year))