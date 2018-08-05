class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count=0
        res = ''
        for i in xrange(0,len(s), k):
            end = min(i+k, len(s))
            if count%2==0:
                res += s[i:end][::-1]
            else:
                res += s[i:end]
            count+=1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.reverseStr(s = "abcdefg", k = 2)