from random import randint
from time import time


def generate_test(number, start, end):
    arr = []
    for i in range(number):
        arr.append(randint(start, end))
    return arr

def get_time(function, array):
    s_time = time()
    function(array)

def sorting_test(function, start = 0, end = 100000):
    for x in [10, 20, 50, 1000, 10000, 30000, 100000]:
        test_arr = generate_test(x, start, end)