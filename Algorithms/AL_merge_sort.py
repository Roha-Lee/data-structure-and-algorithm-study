def _partition(data):
    mid = int(len(data) // 2)
    return data[:mid], data[mid:]

def _merge(left, right):
    result = []
    left_idx = right_idx = 0
    while True:
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        if left_idx == len(left):
            result.extend(right[right_idx:])
            break
        if right_idx == len(right):
            result.extend(left[left_idx:])
            break
    return result

def merge_sort(data):
    if len(data) > 1:
        left, right = _partition(data)
        left = merge_sort(left)
        right = merge_sort(right)
        return _merge(left, right)
    else:
        return data

if __name__ == '__main__':
    print(merge_sort([]))
    print(merge_sort([1]))
    list1 = [1,2,10,4,5,1]
    print(merge_sort(list1))
