# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ordered = self.traverseBST(root)
        res = sum((x for x in ordered if x >= low and x <= high))
        return res
    
    def traverseBST(self, root: TreeNode):
        if root == None:
            return []
        return [
            *self.traverseBST(root.left),
            root.val,
            *self.traverseBST(root.right)
        ]
