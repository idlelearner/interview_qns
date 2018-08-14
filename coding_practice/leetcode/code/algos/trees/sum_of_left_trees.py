# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/sum-of-left-leaves/description/
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0
        if root!=None:
            if root.left!=None:
                left = root.left
                if left.left is None and left.right is None:
                    s += left.val
            s+= self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
            return s
        else:
            return 0
