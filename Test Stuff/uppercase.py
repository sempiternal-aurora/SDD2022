import random

def str_to_upper(string):
    uppercase_string = ''
    for i in string:
        val = ord(i)
        if val >= 97 and val <= 122:
            val -= 32
        uppercase_string += chr(val)
    return uppercase_string

def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    random_string = ''
    for i in range(length):
        random_string += chr(random.randint(0, 127))
    return random_string

if __name__ == '__main__':
    test_strings = []
    for i in range(0, 100):
        test_strings.append(generate_random_string(1, 100000))
    for i in test_strings:
        test = str_to_upper(i)
        if test != i.upper():
            print("Input:", i, "| Output:", test)