class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = [0]*(n+1)
        def climb(n):
            print n, st[n]
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 2
            else:
                if st[n] == 0:
                    st[n] = climb(n-2) + climb(n-1)
                    print n, st[n]
                return st[n]
            
        return climb(n)

if __name__=='__main__':
    s = Solution()
    print s.climbStairs(4)