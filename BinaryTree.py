#!/bin/usr/python3

class BinaryTree(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
    def get_node_value(self):
        return self.value
        
    def set_node_value(self,value):
        self.value = value
        
    def get_left_child(self):
        return self.left
        
    def get_right_child(self):
        return self.right
        
    def insert_left_child(self,left):
        if self.left is None:
            self.left = BinaryTree(left)
            
        else:
            new_node = BinaryTree(left)
            self.left = new_node
            new_node.left = self.left
        
    def insert_right_child(self,right):
        if self.right is None:
            self.right = BinaryTree(right)
        else:
            new_node = BinaryTree(right)
            self.right = new_node
            new_node.right = self.right
            
    @static
    def inorder(tree):
        if tree is not None:
            inorder(tree.get_left_child())
            print(tree.get_node_value())
            inorder(tree.get_right_child())
    @static      
    def preorder(tree):
        if tree is not None:
            print(tree.get_node_value())
            preorder(tree.get_left_child())
            preorder(tree.get_right_child)
            
    @static
    def postorder(tree):
        if tree is not None:
            postorder(tree.get_left_child())
            postorder(tree.get_right_child())
            postorder(tree.get_node_value)
            
