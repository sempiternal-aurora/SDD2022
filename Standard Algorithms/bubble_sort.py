import random

def generate_random_int_list(number):
    new_list = [random.randint(0, 100) for i in range(number)]
    return new_list

def swap_list_values(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def bubble_sort(arr):
    swap = True
    upper = len(arr) - 1
    while swap:
        swap = False
        for i in range(upper):
            if arr[i] > arr[i+1]:
                swap = True
                arr = swap_list_values(arr, i, i+1)
        upper -= 1
    return arr

if __name__ == "__main__":
    list = generate_random_int_list(10)
    print(list)
    sorted_list = bubble_sort(list)
    print(sorted_list)