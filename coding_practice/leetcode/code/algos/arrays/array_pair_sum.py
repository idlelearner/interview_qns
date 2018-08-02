# https://leetcode.com/problems/array-partition-i/description/
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in xrange(0,len(nums),2):
            sum+=nums[i]
        
        return sum