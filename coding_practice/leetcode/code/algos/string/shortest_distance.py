class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        letter_index = [i for i, c in enumerate(S) if c==C]
        res = [len(S)] * len(S)
        for i in range(len(S)):
            for j in letter_index:
                res[i] = min(res[i], abs(j-i))

        return res

if __name__=='__main__':
    s = Solution()
    print s.shortestToChar(S = "loveleetcode", C = 'e')