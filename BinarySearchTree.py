 class BinarySearchTree(object):
        
        def __init__(self,value,parent = None):
            self.left = None
            self.right = None
            self.value = value
            self.parent = None
            
        def get_node_value(self):
            return self.value
        
        def set_node_value(self,value):
            self.value = value
        
        def get_left_child(self):
            return self.left
        
        def get_right_child(self):
            return self.right
        

        def binary_insert(self,item):
            if self is None:
                self = BinarySearchTree(item)
            
            elif self.value is None:
                self.value = item
                self.left = None
                self.right = None
            
            elif self.value > item:
                self.left.binary_insert(item)
                
            else:
                self.right.binary_insert(item)
        
        def find_root(self):
            if self.parent is None:
                return self
            else:
                return self.parent.find_root()