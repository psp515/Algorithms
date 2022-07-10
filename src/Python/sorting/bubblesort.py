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

Algoritms swpas two next elements if for i < j, arr[i] > arr[j]. It means witch each iteration 1 element 
is displaced to its sortet position.

Best Complexity O(n)
Avg. Complexity: O(n^2)
Worst Complexity O(n^2)

"""
def bubblesort(arr):
    swaps = 1
    n = len(arr)
    while swaps > 0: # if there were no swaps everything is sorted
        swaps = 0
        for i in range(1, n):
            # swapping
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swaps += 1


def test():
    sorting_test.sorting_test(bubblesort, [10, 100, 1000, 4000])