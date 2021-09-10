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

    def push(self, data, location=-1):
        curr = self.head
        if location == 0:
            self.head = Node(data)
            self.head.next = curr
            return
        index = 0
        while curr.next and not index == location - 1:
            curr = curr.next
            index += 1            
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def pop(self, location=-1):
        curr = self.head
        prev = self.head
        if not curr:
            print("Empty LinkedList!")
            return 
    
        if location == 0 or not curr.next:
            self.head = curr.next
            del curr
            return 

        index = 0
        while curr.next and not index == location:
            prev = curr
            curr = curr.next 
            index += 1
        prev.next = curr.next
        del curr

                
if __name__ == '__main__':
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

    # push test
    linked_list.push(5, 0)
    print(linked_list)
    linked_list.push(6, 1)
    print(linked_list)
    linked_list.push(7, 3)
    print(linked_list)

    # pop test
    linked_list.pop()
    print(linked_list)
    linked_list.pop(0)
    print(linked_list)
    linked_list.pop(2)
    print(linked_list)
    linked_list.pop(9)
    print(linked_list)

    # test2
    linked_list2 = LinkedList(Node(1))
    print(linked_list2)
    linked_list2.pop()
    print(linked_list2)
    linked_list2.pop()