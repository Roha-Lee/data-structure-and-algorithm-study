def bubble_sort(data):
    for i in range(len(data)):
        num_swap = 0
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                num_swap += 1
        if num_swap == 0:
            return 

def selection_sort(data):
    for i in range(len(data)-1):
        min_value = data[i]
        min_index = i
        for j in range(i, len(data)):
            if data[j] < min_value:
                min_value = data[j]
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i-1, -1, -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            else:
                break
            
if __name__ == '__main__':
    def sort_test(data, sort_method):
        sort_data = data[:]
        sort_method(sort_data)
        print('data:\t%s'%data)
        print('sorted:\t%s'%sort_data)
    
    data = [3,4,1,5,6]
    sort_test(data, bubble_sort)
    sort_test(data, selection_sort)
    sort_test(data, insertion_sort)

