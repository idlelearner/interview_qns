

def binary_search(arr, elmt, st, end):
    if st>end:
        return -1
    mid = st + (end - st)/2
    if arr[mid] == elmt:
        return mid
    if arr[mid] > elmt:
        return binary_search(arr, elmt, st, mid-1)
    else:
         return binary_search(arr, elmt, mid+1, end)

if __name__ == '__main__':
    arr = (1, 3,5,7,9)
    print binary_search(arr, 9, 0, len(arr)-1)
