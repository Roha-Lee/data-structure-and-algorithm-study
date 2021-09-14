def algorithm_1(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i    
    return sum

def algorithm_2(num):
    return int(num * (num + 1) / 2)

if __name__ == '__main__':
    import time 
    N = 1000000
    
    start_time = time.time()
    algorithm_1(N)
    end_time = time.time()
    print('algo - 1 : %.6fs' %(end_time - start_time))
    start_time = time.time()
    algorithm_2(N)
    end_time = time.time()
    print('algo - 2 : %.6fs' %(end_time - start_time))
    