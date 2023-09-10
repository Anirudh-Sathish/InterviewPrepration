# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 08:11:28 2023

@author: aniru
"""

# script to check if given two strings they are permutation of one another

def character_count(str1,str2):
    char_array1 = [0]*128
    char_array2 = [0]*128
    for s in str1:
        char_array1[ord(s)]+=1
    for s in str2:
        char_array2[ord(s)]+=1
    for i in range(128):
        if char_array1[i] != char_array2[i]:
            return False
    return True
def check_permutation(str1,str2,mode):
    if len(str1)!= len(str2):
        return False
    if mode == 1:
        return character_count(str1, str2)
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    for i in range(len(str1_sorted)):
        if str1_sorted[i] != str2_sorted[i]:
            return False
    return True

str1 = "kafka"
str2 = "kanak"

result = check_permutation(str1, str2, 1)
print(result)
    