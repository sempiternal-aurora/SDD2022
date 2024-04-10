import random as rand

def swap_elements(array, key1, key2):
    temp = array[key1]
    array[key1] = array[key2]
    array[key2] = temp
    return array
    

def bubble_sort(array):
    swap = True
    end = len(array) - 1
    while swap:
        swap = False
        for i in range(0, end):
            if array[i] > array[i+1]:
                array = swap_elements(array, i, i+1)
                swap = True
        end = end - 1
    return array

def insertion_sort(array):
    max_index = len(array) - 1
    for next_element in range(max_index-1, -1, -1):
        low = next_element + 1
        high = max_index
        while low <= high:
            middle = (low + high)//2
            if array[middle] > array[next_element]: high = middle - 1
            else: low = middle + 1
        if array[middle] > array[next_element]: middle -= 1
        for i in range(next_element, middle):
            array = swap_elements(array, i, i+1)
    return array

def selection_sort(array):
    start_sorted = len(array) - 1
    while start_sorted > 0:
        max_key = 0
        for i in range(1, start_sorted + 1):
            if array[i] > array[max_key]:
                max_key = i
        swap_elements(array, max_key, start_sorted)
        start_sorted -= 1
    return array

array = [ rand.randint(0, 100) for i in range(0, 10) ]
#array = [4, 5, 8, 1, 3, 7, 5, 9]

print(array)

array = insertion_sort(array)

print(array)


