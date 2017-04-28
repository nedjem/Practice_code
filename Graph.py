#!/bin/usr/python3

class Node(object):
    def __init__(self,name):
        self.neighbours = []
        self.visited = False
        self.name = name
        
        
class Graph1(object):
    
    def __init__(self):
        self.graph_dict = {}
        

    def depth_first_search(self,start):
        if self is None:
            return 0
        
        visit(start)
        start.visited = True
        for neighbour_node in start.neighbours:
            if neighbour_node.visited is False:
                depth_first_search(neighbour_node)
                

    def find_path(self,start,end,path=[]):
        if start is end:
            return None
        if start.value not in self.graph_dict:
            return None
        path.append(start)
        
        for list1 in self.graph_dict[start]:
            for node in list1:
                if node.name not in path:
                    new_path = find_path(node,end)
                    if new_path:
                        return new_path
                        
        return None    
        
class Vertex(object):
    def __init__(self):
        self.distance = None
        self.predecessor = None
        self.marked = False
        self.neighbours = []
        
class Graph2(object):
    def __init__(self):
        self.graph_dict = {}
        
    def breadth_first_search(self,start):
        if self is None:
            return 0
            
        que = Queue()
        start.marked = True
        que.add(start)
        while not que:
            node = que.remove()
            visit(node)
            for n in node.neighbours:
                if node.marked is False:
                    node.marked = True
                    que.remove(node)
    
    
    
    
    
    
    