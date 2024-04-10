class friend():
    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob
    
    def __str__(self):
        return self.fname + "," + self.lname + "," + self.dob

def create_file_number_range(first, last, name):
    file = open(name, "r+")
    for i in range(first, last+1):
        file.write(str(i)+"\n")
    file.close()


def read_file_text(name):
    file = open(name, "r")
    for i in file:
        print(i.strip("\n"))
    file.close()

def open_dob_file(name):
    file = open(name, "r")
    dob_name_list = []
    line = file.readline()
    while line:
        dob_name_list.append(line)
        line = file.readline()
    file.close()
    return dob_name_list

def format_dob_list(dob_name_list):
    friends = []
    for i in range(1, len(dob_name_list)):
        new_friend = dob_name_list[i]
        new_friend = new_friend.strip("\n").split(",")
        new_friend = friend(new_friend[0], new_friend[1], new_friend[2])
        friends.append(new_friend)
    return friends

def swap_list_values(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array

def bubble_sort_friends_name(arr):
    swap = True
    upper = len(arr) - 1
    while swap:
        swap = False
        for i in range(upper):
            if arr[i].lname > arr[i+1].lname:
                swap = True
                arr = swap_list_values(arr, i, i+1)
        upper -= 1
    return arr

def binary_search_name(arr, fname, lname):
    lower = 0
    higher = len(arr) - 1
    found = False
    while (not found) and lower <= higher:
        middle = int((lower+higher)*0.5)
        found = arr[middle].fname+arr[middle].lname == fname+lname
        if found: break
        elif lname > arr[middle].lname: 
            lower = middle + 1
        else: higher = middle - 1
    return found, middle

if __name__ == "__main__":
    create_file_number_range(1, 10, "data.txt")
    read_file_text("data.txt")
    list_thingy = open_dob_file("DOB_Name_people.csv")
    friends = format_dob_list(list_thingy)
    print("\n")
    for i in friends:
        print(i)

    # Sort the friends by name
    friends = bubble_sort_friends_name(friends)
    for i in friends:
        print(i.fname)
    # Find Brad, Mr Marsh and lucas
    has_brad, where_brad = binary_search_name(friends, "Bradley", "Adams")
    if has_brad:
        brad = friends[where_brad]
        print(f"{brad.fname} {brad.lname} was found at position {where_brad} and was born on {brad.dob}")
    else:
        print("Brad was not found")


    has_marshey, where_marshey = binary_search_name(friends, "Jonathon", "Marsh")
    if has_marshey:
        marsh = friends[where_marshey]
        print(f"{marsh.fname} {marsh.lname} was found at position {where_marshey} and was born on {marsh.dob}")
    else:
        print("Marshey was not found")

    has_lucas, where_lucas = binary_search_name(friends, "Lucas", "Wilke")
    if has_lucas:
        lucas = friends[where_lucas]
        print(f"{lucas.fname} {lucas.lname} was found at position {where_lucas} and was born on {lucas.dob}")
    else:
        print("Marshey was not found")