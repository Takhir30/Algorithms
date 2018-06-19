import time
import random


def bubblesort(array):
    m = len(array)-1
    for j in range(len(array)-1):
        for i in range(m):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        m -= 1
    return array


def quicksort(array):
    pivot = array[-1]
    index_pivot = len(array) - 1
    index = 0
    while index < index_pivot:
        if array[index] < pivot:
            index += 1
        elif array[index] > pivot:
            array[index], array[index_pivot-1] = array[index_pivot-1], array[index]
            array[index_pivot], array[index_pivot-1] = array[index_pivot-1], array[index_pivot]
            index_pivot -= 1
        else:
            index += 1
    if index_pivot == 1:
        if len(array) == 2:
            return array
        else:
            return array[:2] + quicksort(array[2:])
    elif index_pivot == 0:
        if len(array) == 1:
            return [pivot]
        else:
            return [pivot] + quicksort(array[1:])
    elif index_pivot == len(array) - 2:
        return quicksort(array[:-2]) + array[-2:]
    elif index_pivot == len(array) - 1:
        return quicksort(array[:-1]) + [pivot]
    else:
        return quicksort(array[:index_pivot]) + [pivot] + quicksort(array[index_pivot+1:])







test_array = [random.randrange(10,10000) for _ in range(9000)]

start_1 = time.time()
print(start_1)
a = quicksort(test_array)
print(time.time()-start_1)

start_2 = time.time()
print(start_2)
b = bubblesort(test_array)
print(time.time()-start_2)

if a == b:
    print('Yes')
