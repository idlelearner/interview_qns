class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        st = sorted(s)
        ts = sorted(t)
        i=0
        while(i<len(st)):
            if st[i]!=ts[i]:
                return ts[i]
            i+=1
        return ts[i]