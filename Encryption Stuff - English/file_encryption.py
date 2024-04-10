def to_bytes_list(int_list):
    bytes_list = []
    for l in int_list:
        new_bytes = bytes(l)
        bytes_list.append(new_bytes)
    return bytes_list

def to_int_list(bytes_list) -> list:
    int_list = []
    for i in range(len(bytes_list)):
        new_list = []
        for b in bytes_list[i]:
            new_list.append(b)
        int_list.append(new_list)
    return int_list

def open_file(target) -> list:
    file = []
    with open(target, 'rb') as f:
        for i in f:
            file.append(i)
    return file

def open_encrypted_file(target):
    with open(target, 'r') as f:
        for i in f:
            file = i
    return file

def str_to_encrypted_list(data):
    data = data.strip("]")
    data = data.replace("[", "")
    encrypted_list = data.split("]")
    for i in range(len(encrypted_list)):
        encrypted_list[i] = encrypted_list[i].split(", ")
    for l in range(len(encrypted_list)):
        for s in range(len(encrypted_list[l])):
            encrypted_list[l][s] = encrypted_list[l][s].strip("'")
    return encrypted_list

def write_encrypted_file(target, data):
    with open(target, "x") as f:
        for i in data:
            f.write(str(i))

def write_file(target, data):
    with open(target, "xb") as f:
        for i in data:
            f.write(i)

def xor(character, key):
    code = ord(character) ^ ord(key)
    result = chr(code)
    return result

def encrypt_xor(number, key):
    encrypted = ''
    for c in number:
        encrypted += xor(c, key)
    return encrypted

def encrypt_int_list(int_list, key):
    encrypted_list = []
    for i in range(len(int_list)):
        new_list = []
        for i in int_list[i]:
            encrypted = encrypt_xor(str(i), key)
            new_list.append(encrypted)
        encrypted_list.append(new_list)
    return encrypted_list

def decrypt_int_list(str_list, key):
    decrypted_list = []
    for i in range(len(str_list)):
        new_list = []
        for i in str_list[i]:
            encrypted = encrypt_xor(i, key)
            encrypted = int(encrypted)
            new_list.append(encrypted)
        decrypted_list.append(new_list)
    return decrypted_list
    
def to_encrypted_bytes_list(int_list):
    bytes_list = []
    for l in int_list:
        bytes_list.append(bytes(l))
    return bytes_list