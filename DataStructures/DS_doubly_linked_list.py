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
        while curr.next and index < location - 1:
            curr = curr.next
            index += 1
            print(curr)
        
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
        pass

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
        for i in range(5):
            doubly_linked_list.push(i)
        doubly_linked_list.push(3.5, 3)
        print(doubly_linked_list)
    
    # node_test()
    # list_generation_test()
    list_push_test()