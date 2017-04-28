#!/usr/bin/python3

class Queue(object):
    
    def __init__(self):
        self.list = []
        
    def add(self,item):
        self.list.append(item)
    
    def remove(self):
        return self.list.pop(0)
    
    "return the top of the queue"
    def peek(self):
        return self.list[0]
        
    def is_empty(self):
        if not self.list:
            return True