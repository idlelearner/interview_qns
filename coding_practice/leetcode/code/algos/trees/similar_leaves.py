# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode.com/problems/leaf-similar-trees/description/
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = []
        seq2 = []
        self.leaf_seq(root1, seq1)
        self.leaf_seq(root2, seq2)
        return seq1 == seq2

    def leaf_seq(self, root, s):
        if root:
            if root.left is None and root.right is None:
                s+=[root.val]
            self.leaf_seq(root.left, s)
            self.leaf_seq(root.right, s)


if __name__ == '__main__':
    root1 = TreeNode(4)
    root1.left = TreeNode(3)
    root1.right = TreeNode(5)

    root2 = TreeNode(4)
    root2.left = TreeNode(7)
    root2.right = TreeNode(5)

    s = Solution()
    print s.leafSimilar(root1, root2)