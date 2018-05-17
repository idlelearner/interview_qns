'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def find_missing_positive_integer(lst):
    if len(lst)==1:
        return 1 if lst[0]!=1 else 2 
    for i in range(0,len(lst)):
        #print i
        if 0 <= lst[i] < len(lst):
            if 0 <= lst[lst[i]] < len(lst):
                lst[lst[lst[i]]] = 0
            lst[lst[i]] = 0

    for i in range(1,len(lst)-1):
        if lst[i]!=0:
            return i
    return len(lst)


if __name__=='__main__':
    print find_missing_positive_integer([3, 4, -1, 1])
    print find_missing_positive_integer([1, 2 , 0])
    print find_missing_positive_integer([1])
    print find_missing_positive_integer([0])
