# call stack example
def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data - 1)
        print('returned', data)

recursive(4)
'''
4
3
2
1
0
ended
returned 0
returned 1
returned 2
returned 3
returned 4
'''

# Stack with Python list 
normal_stack = []
normal_stack.append(1)
normal_stack.append(2)
normal_stack.append(3)
print(normal_stack.pop()) # 3
print(normal_stack.pop()) # 2

'''
Exercise
Implement push and pop of Stack with Python list.
(Do not use the list method pop and append.)
'''
class Stack:
    def __init__(self, max_size):
        self.data_list = [0] * max_size
        self.max_size = max_size
        self.current_idx = -1
    
    def __len__(self):
        if self.current_idx >= 0:
            return self.current_idx + 1
        else:
            return 'Empty'

    def push(self, x):
        if self.current_idx + 1 < self.max_size:
            self.current_idx += 1
            self.data_list[self.current_idx] = x
        else:
            print('Cannot push element. Stack is full.')

    def pop(self):
        if self.current_idx >= 0:
            out_data = self.data_list[self.current_idx]
            self.current_idx -= 1
            return out_data
        else:
            return 'Error'
        

if __name__ == '__main__':
    my_stack = Stack(3)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)
    my_stack.push(5) # stack is full
    print(len(my_stack)) # 3
    print(my_stack.pop()) # 1
    print(my_stack.pop()) # 2
    print(my_stack.pop()) # 3
    print(my_stack.pop()) # Error

