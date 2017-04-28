#!/bin/usr/python3

def is_unique(test_string):
    string = teststring
    
    for char1 in string:
        for char2 in string:
            if char1 == char2:
                unique = True
                
            else:
                unique = False
    return unique
    
def is_unique(test_string):
    string = test_string
    unique_dict = {}
    isUnique = True
    
    count = 0
    for char in string:
        if char in dict: 
            dict[char] = dict[char] + 1
            
        else:
            dict[char] = 0
            
    for key in unique_dict:
        if unique_dict[key] > 0:
            isUnique = False
            
    return isUnique
        
        
    
