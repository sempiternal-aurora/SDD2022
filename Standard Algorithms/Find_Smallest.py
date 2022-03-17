def find_minimum(number_array):
    """
    Takes in any array or list of numbers, and iterates through it to find the smallest value in the array
    """
    position = 0 # Start at the first position, assume it is the highest that we know of
    for i in range(1, len(number_array)): #Iterate through every position in the array after the first
        if number_array[i] < number_array[position]: position = i #if the value at this position is smaller than the previous smallest value, set it as the new smallest value
    return position, number_array[position] #return the position of the smallest value, and the actual smallest value