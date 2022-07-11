from random import randint
from time import time


def generate_test(number, start, end):
    arr = []
    for i in range(number):
        arr.append(randint(start, end))
    return arr

def testit(function, arr, showarr):
    arrcpy = arr.copy()

    s_time = time()
    arrcpy.sort()
    e_time1 = time() - s_time

    s_time = time()
    function(arr)
    e_time2 = time() - s_time

    issuccesfull = arrcpy == arr
    if showarr:
        print(arr)
    print("Is succesfull:", issuccesfull)
    print("Sort time:", round(e_time2, 3))
    print("Standard sort time:", round(e_time1, 3))

    return issuccesfull

def sorting_test(function, tests=[10,100,1000,10000,100000], showarr = False, start = 0, end = 100000):
    print("---------", function.__name__, "---------------------------")
    sum = 0
    for x in tests:
        test_arr = generate_test(x, start, end)
        if showarr:
            print(test_arr)
        sum += testit(function, test_arr,showarr)

    print("Test:", len(tests))
    print("Success:", sum)
