import queue

# Noraml Queue
normal_queue = queue.Queue()

# Enqueue
normal_queue.put('A')
normal_queue.put('B')

print(normal_queue.qsize()) # 2
print(normal_queue.get()) # 'A'
print(normal_queue.qsize()) # 1

# LifoQueue
lifo_queue = queue.LifoQueue()

lifo_queue.put('A')
lifo_queue.put('B')

print(lifo_queue.qsize()) # 2
print(lifo_queue.get()) # 'B'

# Priority Queue
priority_queue = queue.PriorityQueue()

priority_queue.put((10, 'A')) # (priority, data)
priority_queue.put((5, 'B')) # 낮은 숫자일수록 높은 우선순위
priority_queue.put((15, 'C'))

print(priority_queue.qsize()) # 3
print(priority_queue.get()) # (5, 'B')

'''
Exercise 
Implement enqueue, dequeue of Queue with Python list. 
'''
class ListQueue:
    def __init__(self):
        self.list_queue = []

    def __len__(self):
        return len(self.list_queue)

    def enqueue(self, x):
        self.list_queue.append(x)

    def dequeue(self):
        if self.list_queue:
            return self.list_queue.pop(0)
        return "Error"
    

if __name__ == '__main__':
    list_queue = ListQueue()
    list_queue.enqueue(1)
    list_queue.enqueue(3)
    list_queue.enqueue(2)
    print(len(list_queue)) # 3
    print(list_queue.dequeue()) # 1
    print(list_queue.dequeue()) # 3
    print(len(list_queue)) # 1 
    print(list_queue.dequeue()) # 2
    print(len(list_queue)) # 0
    print(list_queue.dequeue()) # Error