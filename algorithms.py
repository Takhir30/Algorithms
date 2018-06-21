import time
import random

def timer(function, array):
    start_time = time.time()
    function(array)
    print(f'{function.__name__} - {time.time()-start_time}')


def bubblesort(array):
    for j in range(len(array)-1, 0, -1):
        for i in range(j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return array


def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def quicksort(array):
      if len(array) < 2:
          return array

      else:
          pivot = array[0]
          less = quicksort([i for i in array[1:] if i <= pivot])
          greater = quicksort([i for i in array[1:] if i > pivot])
          return less + [pivot] + greater


test_array = [random.randrange(10,2000) for _ in range(1000)]


timer(bubblesort, test_array)

timer(quicksort, test_array)

timer(mergesort, test_array)
