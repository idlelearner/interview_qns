# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if (sum == root.val and root.left is None and root.right is None):
            return True
        sum-=root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    print s.hasPathSum(t,0)

        