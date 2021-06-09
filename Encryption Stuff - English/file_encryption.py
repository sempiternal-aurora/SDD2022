def to_bytes_list(int_list) -> list:
    #converts a list of lists of integers to a list of bytes (The python bytes class, or an immutable array of integers up to 255 in value)
    bytes_list = []
    for l in int_list:
        new_bytes = bytes(l)
        bytes_list.append(new_bytes)
    return bytes_list

def to_int_list(bytes_list) -> list:
    #converts a list of bytes to a list of lists of integers
    int_list = []
    for i in range(len(bytes_list)):
        new_list = []
        for b in bytes_list[i]:
            new_list.append(b)
        int_list.append(new_list)
    return int_list

def open_file(target) -> list:
    #reads each line of a file as a bytes python object, and appends them to a list, creating a 'bytes list'
    file = []
    with open(target, 'rb') as f:
        for i in f:
            file.append(i)
    return file

def open_encrypted_file(target) -> str:
    #opens a file and stores all of the plain text as a string
    with open(target, 'r') as f:
        for i in f:
            file = i
    return file

def str_to_encrypted_list(data) -> list:
    #takes a string that is supposed to be a list of lists of strings, and makes it so
    data = data.strip("]")
    data = data.replace("[", "")
    encrypted_list = data.split("]")
    for i in range(len(encrypted_list)):
        encrypted_list[i] = encrypted_list[i].split(", ")
    for l in range(len(encrypted_list)):
        for s in range(len(encrypted_list[l])):
            encrypted_list[l][s] = encrypted_list[l][s].strip("'")
    return encrypted_list

def write_encrypted_file(target, data) -> None:
    #takes a list of strings and writes them to a new file of the target
    with open(target, "x") as f:
        for i in data:
            f.write(str(i))

def write_file(target, data) -> None:
    #Takes a list of bytes, and creates a new file at the target with all of the bytes as the data
    with open(target, "xb") as f:
        for i in data:
            f.write(i)

def xor(character, key) -> str:
    #preforms the xor algorithm on the character and with the key
    code = ord(character) ^ ord(key)
    result = chr(code)
    return result

def encrypt_xor(string, key) -> str:
    #takes a string, and cycles through each character in the string, preforming the xor algorithm on each
    encrypted = ''
    for c in string:
        encrypted += xor(c, key)
    return encrypted

def encrypt_int_list(int_list, key) -> list:
    #takes a list of lists of somethings and encrypts each parts of those lists with the xor algorithm
    encrypted_list = []
    for i in range(len(int_list)):
        new_list = []
        for i in int_list[i]:
            encrypted = encrypt_xor(str(i), key)
            new_list.append(encrypted)
        encrypted_list.append(new_list)
    return encrypted_list

def decrypt_int_list(str_list, key) -> list:
    #takes a list of lists of strings, and decrypts each string to become a list of lists of integers
    decrypted_list = []
    for i in range(len(str_list)):
        new_list = []
        for i in str_list[i]:
            encrypted = encrypt_xor(i, key)
            encrypted = int(encrypted)
            new_list.append(encrypted)
        decrypted_list.append(new_list)
    return decrypted_list