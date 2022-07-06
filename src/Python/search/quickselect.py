


def partition(arr, l, r):
     i = l
     for j in range(l, r):
         if arr[j] < arr[r]:
             arr[i], arr[j] = arr[j], arr[i]
             i += 1
         arr[i], arr[r] = arr[r], arr[i]

     return i


def select(arr, k):
    l, r = 0, len(arr)

    while l <= r:
        q = partition(arr, l, r)
        if q == k:
            return arr[q]
        elif k < q:
            r = q - 1
        else:
            l = q + 1
