class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if d.get(i):
                return True
            d[i] = True
        return False