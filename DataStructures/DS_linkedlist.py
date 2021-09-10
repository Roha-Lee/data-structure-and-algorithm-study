# Implementation of Node 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        addr = 'Null' if (self.next == None) else hex(id(self.next))
        return '(%s, %s)'%(self.data, addr)


# Implementation of linked list
class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        result_str = 'head'
        curr = self.head
        while curr:
            result_str += ' → ' + str(curr)
            curr = curr.next
        return result_str

    def push(self, data):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
            

# Link two different nodes.
node1 = Node(1)
node2 = Node(2)
node1.next = node2
linked_list = LinkedList(node1)
print(linked_list)

# Add data to linked list. 
linked_list.push(3)

# Print data of linked list.
print(linked_list)
linked_list.push(4)
print(linked_list)