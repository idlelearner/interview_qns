# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max = A[0]
        peak_i = 0
        for i in xrange(len(A)):
            if max<A[i]:
                max = A[i]
                peak_i = i
        return peak_i