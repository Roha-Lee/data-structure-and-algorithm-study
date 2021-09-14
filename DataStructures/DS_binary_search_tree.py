#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        left_addr = 'Null' if (self.left_child == None) else hex(id(self.left_child))
        right_addr = 'Null' if (self.right_child == None) else hex(id(self.right_child))
        return "(%s←:%s:→%s)"%(left_addr, self.data, right_addr)
    

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def __str__(self):
        curr = self.root
        if not curr:
            return "EMPTY TREE"

        def print_tree(flag, node, level, print_str):
            space = ' ' * (10 * level)
            print_str += '%s↳%s:%s\n'%(space, flag, node.data)
            if node.right_child:
                print_str = print_tree('right', node.right_child, level+1, print_str)
            if node.left_child:
                print_str = print_tree('left', node.left_child, level+1, print_str)
            return print_str
            
        return print_tree('root', curr, 0, '')

    def insert(self, data):
        curr = self.root
        if not curr:
            self.root = Node(data)
            return 
        
        while curr:
            if curr.data < data:
                if not curr.right_child:
                    curr.right_child = Node(data)
                    return 
                curr = curr.right_child
            else:
                if not curr.left_child:
                    curr.left_child = Node(data)
                    return 
                curr = curr.left_child
    
    def search(self, data):
        curr = self.root
        while curr:
            if curr.data == data:
                return curr
            elif curr.data < data:
                curr = curr.right_child
            else:
                curr = curr.left_child
        return 'Not Found!'
    
    
if __name__ == '__main__':
    def node_test():
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3, left_child=node1, right_child=node2)
        print(node1)
        print(node2)
        print(node3)

    def binary_search_tree_insert_search_test():
        bst = BinarySearchTree()
        bst.insert(21)
        bst.insert(35)
        bst.insert(20)
        bst.insert(40)
        bst.insert(22)
        bst.insert(18)
        bst.insert(14)
        print(bst)
        print(bst.search(14))
        print(bst.search(13))
        print(bst.search(22))
        print(bst.search(21))
        
    # node_test()
    binary_search_tree_insert_search_test()
    