

# arr, val, index
arrays = [([5, 8, 9, 10, 123], 5, 0),
          ([7, 8, 9, 10, 12], 12, 4),
          ([5, 8, 9, 10, 12, 15, 34, 1234, 4564, 1242345], 4564, 8)]

def binsearch_test(f):
    print("---------", f.__name__, "---------------------------")
    for i in range(3):
        arrays[i][0].sort()
        x = f(arrays[i][0], arrays[i][1])
        print("Is succesfull:", arrays[i][2] == x)

    x = f([7, 8, 9, 10, 12], 5)
    print("Is succesfull:", -1 == x)

def quickselect_test(f):
    print("---------", f.__name__, "---------------------------")
    for i in range(3):
        x = f(arrays[i][0], arrays[i][2])
        print("Is succesfull:", arrays[i][1] == x)