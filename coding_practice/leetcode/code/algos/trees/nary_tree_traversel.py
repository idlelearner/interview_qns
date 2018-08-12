"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object): 
    res = []
    def generatepostorder(self, root):
        if root:
            for child in root.children:
                self.generatepostorder(child)
            self.res.append(root.val)


    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.generatepostorder(root)
        return self.res