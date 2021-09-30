def binary_search(data, search):
    if len(data) == 0:
        return False
    if len(data) == 1:
        return data[0] == search
    
    mid = int(len(data) // 2)
    if data[mid] == search:
        return True
    return binary_search(data[:mid], search) or binary_search(data[mid+1:], search)
    
if __name__ == '__main__':
    import random
    number_pool = list(range(300))
    random.shuffle(number_pool)
    data = sorted(number_pool[:100])
    print(data)
    print(binary_search(data, 5))
