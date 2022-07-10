from sorting import sorting_test

"""
Problem
------------
Sorting array.

Parameters
----------

arr : Array
    array of items to sort 
    
Algoirthm
---------

Algorithm divides array into 2 sectors sorted and unsorted. Next element for i-th position is searched is 
unsorted array as the lowest item. So witch each iteration of the first for one element is sorted.


Best Complexity O(n^2)
Avg. Complexity: 0(n^2)
Worst Complexity O(n^2)

"""


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]



def test():
    sorting_test.sorting_test(selectionsort, [10, 100, 1000, 4000])