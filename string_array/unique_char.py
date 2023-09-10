# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 07:48:50 2023

@author: aniru
"""

"""
Given a string , check if it has all unique characters

Assumption : The given string contains only ascii
"""

def determine_unique(input_str):
    if len(input_str) > 128:
        return False
    bool_arr = [False]*128
    for s in input_str:
        if bool_arr[ord(s)]:
            return False
        bool_arr[ord(s)] = True
    return True

def determine_unique_withoutds(input_str):
    if len(input_str)>128:
        return False
    for i in range(0,len(input_str)):
        for j in range(i+1,len(input_str)):
            if input_str[i] == input_str[j]:
                return False
    return True
string = "catholxc"
result = determine_unique(string)
print(result)

print(determine_unique_withoutds(string))