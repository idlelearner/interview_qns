# https://leetcode.com/problems/flipping-an-image/discuss/154973/One-line-python-answer
def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-element for element in nested_array][::-1] for nested_array in A]