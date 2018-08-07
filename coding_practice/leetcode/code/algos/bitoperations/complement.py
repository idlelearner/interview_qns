class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_str = bin(num)[2:]
        print bin_str
        comp_str = ''.join(['1' if c=='0' else '0' for c in bin_str])
        print comp_str
        return int(comp_str, 2)

if __name__=='__main__':
    s = Solution()
    print s.findComplement(1)