# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkLeft(self, root, level):
        if not root:
            return []
        else:
            return self.checkLeft(root.left, level+1) + [root.val + level*1000] + self.checkLeft(root.right, level+1)

    def checkRight(self, root, level):
        if not root:
           return []
        else:
            return self.checkRight(root.right, level+1) + [root.val + level*1000] + self.checkRight(root.left, level+1)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkLeft(root.left, 1) == self.checkRight(root.right, 1)
