#!/usr/bin/python3

class node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
        
    def set_data(self,new_data):
        self.data=new_data

    def set_next(self,new_next):
        self.next_node = new_next
        
class linked_list(object):
    def __init__(self,head=None):
        self.head=head
        
    
    def is_empty(self):
        if self.head == None:
            return True
    
    
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def remove(self,item):
        current = self.head
        found = False
        previous = None
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next)
                
    
    def search(self,item):
        current = self.head
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                
        return found

    def deduplicate(self):

        current = link_list.head
         while current.get_next != None:
            next_node = current.get_next()
            while next_node.get_next() != None:
                if current.get_data() == next_node.get_data():
                    current.set_next(next_node.get_next)
                else:
                    next_node = next_node.get_next
                    
            current = current.get_next()

     def return_K_to_last(self,K,n):
        if head == None:
            return 0
        current = self.head
        for i in range(n-1):
            current = current.get_next()
            if ( i == n-k):
                return current.get_data()
            else:
                return 0
                
    def return_K_to_last(self,start=self.head,k):
        if start is None:
            return 0
        
        index = return_K_to_last(start.get_next(),k) + 1
        if index == k:
            return start.get_data()
        
    
    def remove_middle_node(self,node):
        if self.head is None:
            return 0
        
        if node.get_next == None and node == self.head
            return 0
        
        temp = node.get_next()
        node = temp
        del(node)
        
    def partition(self,item):
        lower_list = linked_list()
        higher_list = linked_list()
        
        current = self.head
        while(current.get_next is not None):
            if current.get_data <= item:
                lower_list.insert(data)
                current = current.get_next()
            else:
                higher_list.insert(data)
                current = current.get_next()
                
        new_current = lower_list.head
        while new_current is not None:
            new_current = new_current.get_next()
            
        return new_current.set_next(higher_list.head)
        
    @static
    def sum_list(link_list1, link_list2):
        current1 = link_list1.head
        current2 = link_list2.head
        answer = linked_list()
        
        if current1.get_next is None and current2.get_next is None:
            return None
        carry = 0
        while current1.get_next is not None and current2.get_next is not None:
            value = current1.get_data() + current2.get_data() + carry
            answer.insert(value%10)
            carry = value // 10
            
        return answer
    
    def isPalindrome(self):
            
        current = self.head
        reverse_list = linked_list()
        while current is not None:
            reverse_list.insert(current)
            current = current.get_next
        
        reverse = reverse_list.head    
        while current is not None and reverse is not None:
            if current.get_data() != reverse.get_data():
                return False
            current = current.get_next()
            reverse = reverse.get_next()
            
            if current is None and reverse is None:
                return True
    @static        
    def intersection(link_list1, link_list2):
        current1 = link_list1.head
        current2 = link_list2.head
        
        while current1 is not None:
            count1 += 1
            current1 = currrent1.get_next()
            
        while current2 is not None:    
            count2 += 1
            current2 = current2.get_next()
            
        if current1 is not current2:
            return False
            
        elif count1 < count2:
            current1 = link_list1.head
            current2 = link_list2.head
            diff = count2 - count1
            for i range(diff -1):
                current2 = current2.get_next()
             
        else:
            current1 = link_list1.head
            current2 = link_list2.head
            diff = count1 - count2
            for i in range(diff -1):
                current1 = current1.get_next()
            
        
        while current1.get_next() is not None and current2.get_next() is not None:
            if current1.get_next is current2.get_next:
                current1 = current1.get_next()
                return current1.get_data()
                
            else:
                current1 = current1.get_next()
                current2 = current2.get_next()
                
    def is_looped(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()
            fast = fast.get_next()
            if slow is fast:
                break
        
        """check for no loops"""
        if fast is None or fast.get_next() is None:
            return 0
            
        slow = self.head()
        while slow is not fast:
            slow = slow.get_next()
            fast = fast.get_next()
            
        return slow
    
    def return_K_to_last(self,K,n):
        if head == None:
            return 0
        current = self.head
        for i in range(n-1):
            current = current.get_next()
            if ( i == n-k):
                return current.get_data()
            else:
                return 0
                
    def return_K_to_last(self,start=self.head,k):
        if start == None:
            return 0
        
        index = return_K_to_last(start.get_next(),k) + 1
        if index == k:
            return start.get_data()