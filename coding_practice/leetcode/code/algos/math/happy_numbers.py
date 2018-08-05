class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        visited.add(n)
        sum = n
        for i in range(10000):
            v = sum
            sum = 0
            while v!=0:
                sum += (v%10)**2
                v = v/10
            if sum==1:
                return True
            if sum in visited:
                return False
            visited.add(sum)
        return False
