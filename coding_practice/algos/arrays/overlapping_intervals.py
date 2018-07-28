# https://www.coderbyte.com/algorithm/determine-overlapping-numbers-in-ranges
def OverlappingRanges(arr):
    st1 = arr[0] 
    st2 = arr[2]
    end1 = arr[1]
    end2 = arr[3]

    o_st = max(st1, st2)
    o_end = min(end1, end2)

    if (o_end-o_st)+1 >= arr[4]:
        return 'true'
    return 'false'

print OverlappingRanges([4, 10, 2, 6, 3])
print OverlappingRanges([0]*5)
print OverlappingRanges([10, 20, 4, 14, 4])
print OverlappingRanges([10, 20, 4, 14, 14])