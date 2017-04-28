class Min_Heap2(object):
    
    def __init__(self):
        self.heaplist = [0]
        self.current_size = 0
        
    def bubble_up(self,index):
        while index // 2 > 0:
            if self.heaplist[index] < self.heaplist[index // 2]:
                temp = self.heaplist[index // 2]
                self.heaplist[index // 2] = self.heaplist[index]
                self.heaplist[index] = temp
            index = index // 2
            
    def insert(self,k):
        self.heaplist.append(k)
        self.current_size += 1
        bubble_up(k)
        
    def bubble_down(self,index):
        mc = min_child(self,index)
        while 2*index <= self.current_size:
            if self.heaplist[index] > self.heaplist[mc]:
                temp = self.heaplist[mc]
                self.heaplist[mc] = self.heaplist[index]
                self.heaplist[index] = temp
            index = mc
    
    def min_child(self,i):
        if self.heaplist[2*i] < self.heaplist[2*i + 1]:
            return 2*i
        else:
            return 2*i + 1
        
    def del_min(self):
        return_value = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.current_size]
        self.current_size = self.current_size - 1
        self.heaplist.pop()
        bubble_down(self.heaplist[1])
        return return_value