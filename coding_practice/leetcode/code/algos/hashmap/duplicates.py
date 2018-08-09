# https://leetcode.com/problems/contains-duplicate-ii/description/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if d.get(v):
                d[v].append(i)
                if len(d[v])>1:
                    for j in xrange(1, len(d[v]),1):
                        if (d[v][j] - d[v][j-1])<=k:
                            return True
            else:
                d[v] = [i]
        return False