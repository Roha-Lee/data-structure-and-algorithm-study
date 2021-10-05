def _partition(data):
    pivot = data[0]
    left = []
    right = []
    for elem in data[1:]:
        if elem < pivot: 
            left.append(elem)
        else:
            right.append(elem)
    return left, pivot, right

def quick_sort(data):
    if len(data) <= 1:
        return data
    left, pivot, right = _partition(data)
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    print(quick_sort([]))
    print(quick_sort([1]))
    list1 = [1,2,10,4,5,1]
    print(quick_sort(list1))
