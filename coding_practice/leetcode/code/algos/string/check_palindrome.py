class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #if len(s) == 1: return True
        for i in xrange(0,len(s),1):
            new_str = s[:i] + s[i+1:]
            if new_str == new_str[::-1]:
                return True
        return False

if __name__=='__main__':
    s = Solution()
    print s.validPalindrome("a")