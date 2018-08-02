class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s, e = 0,num
        while s<e:
            m = (s+e)/2
            if m*m==num:
                return True
            elif m==s or m==e:
                return False
            elif m*m>num:
                e=m
            else:
                s=m
            print ' '.join([str(s),str(e)])
        if s*s==num:
            return True
        else:
            return False

# return (num**0.5).is_integer()

if __name__ == '__main__':
    s = Solution()
    print s.isPerfectSquare(25)