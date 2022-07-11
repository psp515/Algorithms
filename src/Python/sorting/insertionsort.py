from sorting import sorting_test
"""
Problem
------------
Sorting array.

Parameters
----------

arr : Array
    array of items to sort 
    
Parameters
----------

arr : Array
    array of items to sort 

Algorithm
---------

Algorithm divides array in two sub arrays sorted and unsorted. 

Best Complexity O(n)
Avg. Complexity: 0(n^2)
Worst Complexity O(n^2)

"""

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test():
    sorting_test.sorting_test(insertionsort,[10, 100, 1000, 4000])