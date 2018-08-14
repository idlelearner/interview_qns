class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        rnums = nums[::-1]
        l = len(nums)
        for n in nums:
            d[n]=d[n]+1
        max_value = max([v for k, v in d.items()])
        print max_value
        max_items = [k for k, v in d.items() if v==max_value]
        print max_items
        min_size = l
        for m in max_items:
            print m
            min_size = min(min_size, ((l-rnums.index(m)-1) - nums.index(m))+1)
        return min_size

if __name__=='__main__':
    s = Solution()
    print s.findShortestSubArray([1,2,2,3,1,4,2])