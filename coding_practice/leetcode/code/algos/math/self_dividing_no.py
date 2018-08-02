# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        i = left
        while i<=right:
            v = i
            while v!=0:
                m = v%10
                if m==0 or i%m!=0:
                    break
                else:
                    v=v/10
            if v==0:
                res.append(i)
            i+=1
        return res

if __name__ == '__main__':
    s=Solution()
    print s.selfDividingNumbers(1,22)