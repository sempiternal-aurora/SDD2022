def insert_name(initial_string, inserted_string):
    """
    For a given string, this function iterates through it to find the first instance of ;, our delimiter, replacing this with a string, inserting it into the original string
    """
    length = len(initial_string) #find the length of the string
    for i in range(length): #iterate through the initial string
        if initial_string[i] == ";": #At the first instance of the character ;
            split_position = i #record the position where the new string is to be inserted
            break #break out of the loop
    first_part = initial_string[:split_position] #seperate out the first part of the string, before the delimiter
    second_part = initial_string[split_position+1:] #seperate out all characters after the delimiter, not including it
    new_string = first_part + inserted_string + second_part #combine the two parts together, with the delimiter replaced with the new string
    return new_string #return the 


if __name__ == "__main__":
    the_greatest_string = "The greatest person to ever exist is ;, they are the most amazing, brilliant and wonderful person, ; is."
    name = "Althaea Angstrom Aliano Alison Animali Arabac Astra Amastacia"
    the_greatest_string = insert_name(the_greatest_string, name)
    the_greatest_string = insert_name(the_greatest_string, name)
    print(the_greatest_string)