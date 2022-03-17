def find_maximum(number_array):
    """
    Takes in any array or list of numbers, and iterates through it to find the largest value in the array
    """
    position = 0 # Start at the first position
    for i in range(1, len(number_array)): #Iterate through every number in the array after the first
        if number_array[i] > number_array[position]: position = i #if the value at this position is greater than the previous maximum value, set it as the new maximum value
    return position, number_array[position] #return the position of the maximum value, and the actual maximum value