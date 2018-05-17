'''
Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def is_sum_present(lst, k):
    s = set()
    for v in lst:
        if abs(k-v) in s:
            return True
        else:
            s.add(v)
    return False

if __name__=='__main__':
    print is_sum_present([10, 15, 3, 7], 17)
    print is_sum_present([10, 15, 3, 7], 18)
    print is_sum_present([10, 15, 3, 7], 19)