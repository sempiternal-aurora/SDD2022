def binary_search(arr, value):
    lower = 0
    higher = len(arr) - 1
    found = False
    while (not found) and lower <= higher:
        middle = int((lower+higher)*0.5)
        found = arr[middle] == value
        if found: break
        elif value > arr[middle]: lower = middle + 1
        else: higher = middle - 1
    if found:
        print("Value found at position", middle)
    else:
        print("Value not found")

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    binary_search(array, 13)
