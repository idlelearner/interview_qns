# https://www.coderbyte.com/algorithm/oddball-sum
def oddball_sum(arr):
    odd_sum = 0
    for i in range(len(arr)):
        if i%2==1:
            odd_sum+=arr[i]

    return odd_sum

print oddball_sum([1,2,3,4,5,6])