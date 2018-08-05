class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = 0
        i1, i2 = 0, 0
        for i, v in enumerate(bin(N)[2:]):
            if v == "1":
                i1 = i2
                i2 = i
                l = max(i2-i1, l)
        return l


if __name__=='__main__':
    s = Solution()
    print s.binaryGap(5)
