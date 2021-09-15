#!/usr/bin/env python
# -*- coding: utf-8 -*-
class MaxHeap:
    def __init__(self):
        self.data = []
    
    def __str__(self):
        if len(self.data) == 0:
            return 'EMPTY HEAP'
        return self._print_heap(1, 0)

    def __len__(self):
        return len(self.data)

    def insert(self, data):
        # insert 
        self.data.append(data)
        self._heapify('insert', len(self.data))

    def remove(self):
        # remove
        if len(self.data) == 0:
            return 'EMPTY HEAP'
        self._swap(1, len(self.data))
        return_data = self.data.pop()
        self._heapify('remove', 1)
        return return_data
    
    def _print_heap(self, index, depth):
        space = ' ' * depth * 10
        position = 'left' if index % 2 == 0 else 'right'
        if index == 1:
            position = "root"

        if index > len(self.data):
            return ''
        else:
            return '%s↳%s:%s\n'%(space, position, self.data[index-1]) + \
                    self._print_heap(index*2+1, depth+1) + \
                    self._print_heap(index*2, depth+1)

    def _swap(self, pos1, pos2):
        self.data[pos1-1], self.data[pos2-1] = self.data[pos2-1], self.data[pos1-1]

    def _heapify(self, method, index=None):
        if method == 'insert':
            if index == 1:
                return 
            else:
                parent_index = int(index//2)
                if self.data[index-1] <= self.data[parent_index-1]: 
                    return 
                else:
                    self._swap(index, parent_index)
                    self._heapify(method, parent_index)

        if method == 'remove':
            if len(self.data) == 0:
                return
            
            if 2*index+1 <= len(self.data): 
                if self.data[2*index-1] < self.data[2*index]:
                    if self.data[index-1] < self.data[2*index]:
                        self._swap(index, 2*index+1)
                        index = 2 * index + 1
                    else:
                        return
                else:
                    if self.data[index-1] < self.data[2*index-1]:
                        self._swap(index, 2*index)
                        index = 2 * index
                    else:
                        return
            elif 2*index <= len(self.data):
                if self.data[index-1] < self.data[2*index-1]:
                    self._swap(index, 2*index)
                else:
                    return
            else:
                return
            self._heapify(method, index)
    
        
if __name__ == '__main__':
    import random 
        
    def heap_insert_test():
        max_heap = MaxHeap()
        for i in range(LENGTH):
            max_heap.insert(random.randint(0, MAX_RANGE)) 
        print(max_heap)
        return max_heap
    
    def heap_remove_test():
        max_heap = heap_insert_test()
        while len(max_heap) > 0:
            print(max_heap.remove())
        print(max_heap.remove())

    MAX_RANGE = 20
    LENGTH = 7

    heap_insert_test()
    print('-'*50)
    heap_remove_test()