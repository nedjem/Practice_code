#!/usr/bin/python3

class Stack(object):
    
    def __init__(self):
       self.list = []
       
    def is_empty(self):
        if not self.list:
            return True
            
    def push(self,item):
        self.list.append(item)
    
    """ pop removes item from end of a list """    
    def pop(self):
        self.list.pop()
        
    def peek(self):
        return self.list[len(self.list)-1]