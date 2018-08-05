# https://leetcode.com/problems/jewels-and-stones/description/
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        tot=0
        for s in S:
            if s in J:
                tot+=1
        return tot