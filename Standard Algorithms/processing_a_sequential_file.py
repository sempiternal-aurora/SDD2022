def create_file_number_range(start, stop, name):
    file = open(name, "w")
    for i in range(start, stop+1):
        file.write(str(i))
    file.close()

if __name__ == "__main__":
    create_file_number_range(1, 10, "data.txt")