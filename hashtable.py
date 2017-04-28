#!/usr/bin/python3

class HashTable(object):
    def __init__(self,size):
        self.table = [[] for i in range(size)]
        self.size = size
    
    def hash_function(self,key):
        sum = 0
        for char in key:
            sum += toASCII(char)
        index = sum % self.size
            
        return index
        
    def store(self,key):
        self.table[self._hashfunction(key)].append(key)
        
    def retrieve(self,key):
        index = self._hash_function(key)
        for i in self.table[index]:
            if i is key:
                return True
            else:
                return False
        
def main():
     hashtable1 = Hashtable(10)
     hashtable.store("joshua")
     hashtable.retrive("joshua")
     
if __name__ == "__main__":
    main()
    