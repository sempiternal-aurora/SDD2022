import random

def generate_random_int_list(number):
    new_list = [random.randint(0, 100) for i in range(number)]
    return new_list

def swap_list_values(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def selection_sort(arr):
    for upper in range(len(arr)-1,-1,-1):
        position = 0
        for i in range(1, upper):
            if arr[i] > arr[position]:
                position = i
        if arr[position] > arr[upper]:
            swap_list_values(arr, position, upper)
    return arr

if __name__ == "__main__":
    list = generate_random_int_list(10)
    print(list)
    sorted_list = selection_sort(list)
    print(sorted_list)