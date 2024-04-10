def find_minimum_and_maximum(number_array):
    """
    Takes in any array or list of numbers, and iterates through it to find the smallest and largest value in the array
    """
    maximum = 0 # Start at the first position, assume it is the highest that we know of
    minimum = 0 # assume that the first value is the smallest we know of
    for i in range(1, len(number_array)): #Iterate through every position in the array after the first
        if number_array[i] < number_array[minimum]: minimum = i #if the value at this position is smaller than the previous smallest value, set it as the new smallest value
        if number_array[i] > number_array[maximum]: maximum = i #if the value at this position is greater than the previous greatest value, set it as the new greatest value
    return maximum, number_array[maximum], minimum, number_array[minimum] #return the position of the maximum and minimum of the array, and their value.