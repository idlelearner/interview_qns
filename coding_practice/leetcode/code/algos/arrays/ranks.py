class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        res = [""]*len(nums)
        for i,num in enumerate(nums):
            d[num]=i
        nums = sorted(nums, reverse=True)
        for i,num in enumerate(nums):
            if i==0:
                res[d[num]] = "Gold Medal"
            elif i==1:
                res[d[num]] = "Silver Medal"
            elif i==2:
                res[d[num]] = "Bronze Medal"
            else:
                res[d[num]] = "%s"%(i+1)
        return res

if __name__=='__main__':
    s = Solution()
    print s.findRelativeRanks([5,4,3,2,1])