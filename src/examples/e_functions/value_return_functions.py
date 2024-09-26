import random

def test_config():
    return True

def echo_value(num):
    return num

def generate_random_value(min_num, max_num):
    random.seed()
    number = random.randint(min_num, max_num)
    return  number