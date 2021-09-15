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
        return '(%s←:%s:→%s)'%(left_addr, self.data, right_addr)
    

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    
    def __str__(self):
        curr = self.root
        if not curr:
            return 'EMPTY TREE'

        def print_tree(flag, node, level, print_str):
            space = ' ' * (10 * level)
            print_str += '%s↳%s:%s\n'%(space, flag, node.data)
            if node.right_child:
                print_str = print_tree('right', node.right_child, level+1, print_str)
            if node.left_child:
                print_str = print_tree('left', node.left_child, level+1, print_str)
            return print_str
            
        return print_tree('root', curr, 0, '')

    def _is_leaf(self, node):
        return not (node.left_child or node.right_child)

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
    
    def remove(self, data):
        curr = self.root
        parent = self.root
        searched = False
        while curr:
            if curr.data == data:
                searched = True
                break
            elif curr.data < data:
                parent = curr
                curr = curr.right_child
            else:
                parent = curr
                curr = curr.left_child
        
        if not searched:
            return 
        
        if not curr.left_child:
            if self.root == curr:
                self.root = curr.right_child
            else:
                if curr.data <= parent.data:
                    parent.left_child = curr.right_child
                else:
                    parent.right_child = curr.right_child
        
        elif not curr.right_child:
            if self.root == curr:
                self.root = curr.left_child
            else:
                if curr.data <= parent.data:
                    parent.left_child = curr.left_child
                else:
                    parent.right_child = curr.left_child
        else:
            target_node = curr.right_child
            target_parent = curr
            
            while target_node.left_child:
                target_parent = target_node
                target_node = target_node.left_child
            # remove target_node
            if curr == target_parent:
                target_parent.right_child = target_node.right_child
            else:
                target_parent.left_child = target_node.right_child
            target_node.right_child = curr.right_child 
            target_node.left_child = curr.left_child

            if self.root == curr:
                self.root = target_node
            else:
                if curr.data <= parent.data:
                    parent.left_child = target_node
                else:
                    parent.right_child = target_node
        del curr
        return 

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

    def binary_search_tree_remove_test():
        bst = BinarySearchTree()
        bst.insert(21)
        bst.insert(10)
        bst.insert(50)
        bst.insert(8)
        bst.insert(17)
        bst.insert(14)
        bst.insert(19)
        bst.insert(1)
        bst.insert(9)
        bst.insert(12)
        bst.insert(15)
        bst.insert(22)
        bst.insert(70)
        bst.insert(13)
        print(bst)
        print('-'*50)
        bst.remove(21)
        print(bst)
        print('-'*50)
        bst.remove(8)
        bst.remove(12)
        bst.remove(10)
        print(bst)
        print('-'*50)
        

    # node_test()
    # binary_search_tree_insert_search_test()
    binary_search_tree_remove_test()
    