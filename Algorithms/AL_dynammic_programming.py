# Recursive Call
def Fibonacci(num):
    if num <= 1:
        return num
    return Fibonacci(num-1) + Fibonacci(num-2)  

# Dynamic Programming - Fibonacci 
def DP_Fibonacci(num):
    cache = [0 for _ in range(num+1)]
    cache[0] = 0
    cache[1] = 1
    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]


def DP_Pascal(rowIndex):
    cache = [1 for _ in range(rowIndex)]
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    for start in range(1, rowIndex):
        for idx in range(start, 0, -1):
            cache[idx] = cache[idx] + cache[idx-1]
    return cache + [1]
        
if __name__ == '__main__':
    import time 
    start_time = time.time()
    Fibonacci(30)
    end_time = time.time()
    print("Recursive: ", end_time - start_time)
    start_time = time.time()
    DP_Fibonacci(30)
    end_time = time.time()
    print("Dynamic Programming: ", end_time - start_time)
    '''
    Recursive:  0.24840807914733887
    Dynamic Programming:  1.3113021850585938e-05
    '''