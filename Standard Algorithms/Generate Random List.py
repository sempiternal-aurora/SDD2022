import random

def generate_random_int_list(number):
    new_list = [random.randint(0, 100) for i in range(number)]
    return new_list