#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

    def __str__(self):
        prev_addr = 'Null' if (self.prev == None) else hex(id(self.prev))
        next_addr = 'Null' if (self.next == None) else hex(id(self.next))
        return '(←%s, %s, %s→)'%(prev_addr, self.data, next_addr)


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.head
        
    def __str__(self):
        curr = self.head
        
        result_str = 'head → '
        while curr:
            if curr == self.head:
                result_str += str(curr)
            else:
                result_str += ' ↔ ' + str(curr)
            curr = curr.next
        result_str += ' ← tail'
        return result_str
    
    def push(self, data, location=-1):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
            return 

        curr = self.head
        if location == 0:    
            self.head = Node(data)
            self.head.next = curr
            curr.prev = self.head
            return 

        index = 0 
        while curr.next and not index == location - 1:
            curr = curr.next
            index += 1
    
        if curr == self.tail:
            curr.next = Node(data)
            self.tail = curr.next
            curr.next.prev = curr
        else:
            temp = curr.next
            new_node = Node(data)
            
            curr.next = new_node
            new_node.prev = curr
            new_node.next  = temp
            temp.prev = new_node

    def pop(self, location=-1):
        curr = self.head
        if not curr:
            print("EMPTY linked list.")
            return 
        if location == 0 or not curr.next:
            self.head = curr.next
            if not curr.next:
                self.tail = self.head
            else:
                curr.next.prev = None
            del curr
            return 

        index = 0
        while curr.next and not index == location:
            curr = curr.next
            index += 1
        if not curr.next:
            curr.prev.next = curr.next
            self.tail = curr.prev
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            del curr
            return 

            
    def remove(self, data):
        pass

    def indexOf(self, data):
        pass
        
if __name__ == '__main__':
    def node_test():
        # Node test
        node1 = Node(3)
        node2 = Node(5)
        node3 = Node(2)
        node1.next = node2
        node2.prev = node1
        node2.next = node3 
        node3.prev = node2
        
        # Node print test
        print(node1, node2, node3)

    def list_generation_test():
        # List generation test
        node1 = Node(1)
        doubly_linked_list = DoublyLinkedList(node1)
        
        # List print test
        print(doubly_linked_list)

    def list_push_test():
        doubly_linked_list = DoublyLinkedList()
        for i in range(3):
            doubly_linked_list.push(i)
        print(doubly_linked_list)
        for i in range(4):
            doubly_linked_list.push(i, 4-i)
        print(doubly_linked_list)   
        doubly_linked_list.push(11, 0)
        doubly_linked_list.push(12)
        print(doubly_linked_list)
    
    def list_pop_test():
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.push(i)
        print(doubly_linked_list)
        doubly_linked_list.pop(2)
        print(doubly_linked_list)
        doubly_linked_list.pop()
        print(doubly_linked_list)
        doubly_linked_list.pop(0)
        print(doubly_linked_list)
        doubly_linked_list.pop(1)
        print(doubly_linked_list)
        doubly_linked_list.pop(0)
        print(doubly_linked_list)
        doubly_linked_list.pop(0)
        print(doubly_linked_list)

    # node_test()
    # list_generation_test()
    # list_push_test()
    # list_pop_test()