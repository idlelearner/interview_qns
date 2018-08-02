class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for v in moves:
            if v=="U":
                y+=1
            if v=="D":
                y-=1
            if v=="L":
                x-=1
            if v=="R":
                x+=1      
        
        return (x==0 and y==0)

if __name__=='__main__':
    s = Solution()
    print s.judgeCircle("UD")
