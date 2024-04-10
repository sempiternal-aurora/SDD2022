import random

def generate_random_int_list(number):
    new_list = [random.randint(0, 100) for i in range(number)]
    return new_list

def swap_list_values(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        lower = 0
        upper = i - 1
        while lower <= upper:
            middle = (lower + upper)//2
            if arr[i] >= arr[middle]: lower = middle + 1
            else: upper = middle - 1
        if arr[i] >= arr[middle]:
            position = middle + 1
        else: position = middle
        for j in range(i, position, -1):
            swap_list_values(arr, j, j-1)
    return arr

def is_sorted(arr):
    flag = False
    for i in range(len(arr)-1):
        if(arr[i] > arr[i + 1]):
            flag = True
    return flag
    

if __name__ == "__main__":
    works = True
    i = 0
    file = open("Sorting_list_data.txt", 'a+')
    while works and i < 10000:
        list = generate_random_int_list(10)
        file.write(list)
        sorted_list = binary_insertion_sort(list)
        works = not is_sorted(sorted_list)
        i += 1