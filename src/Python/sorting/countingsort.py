from sorting import sorting_test
"""
Problem
------------
Sorting array.

Parameters
----------

arr : Array
    array of items to sort 
    
Algorithm
---------

Algorithm creates new array with length of biggest number in array ant then simply counts number of 
elements of index value.

Best Complexity O(n)
Avg. Complexity: O(n)
Worst Complexity O(n)

* we have to assume first that all elements are lower than length of array and minimal element is > 0 or we can 
shift this range yet then time complexity is bigger.

"""

def countingsort(arr):
    n = len(arr)
    count_arr = [0 for _ in range(n)]
    sorted_arr = [0 for _ in range(n)]

    for i in arr:
        count_arr[i] += 1

    for i in range(1, n):
        count_arr[i] += count_arr[i-1]

    for i in range(n):
        sorted_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1

    for i in range(n):
        arr[i] = sorted_arr[i]


def test():
    sorting_test.sorting_test(countingsort, [1000000], False, 0, 9)