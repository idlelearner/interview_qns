# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i, val in enumerate(nums):
            if h.get(val) is None:
                h[val]=i
            if not h.get(target-val) is None and h[target-val]!=i:
                return [h[target-val], i]
        
        return []

s = Solution()
l = (1,2,3)
t = 3
print s.twoSum(l, t)
