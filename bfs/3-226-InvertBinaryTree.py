class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            l = self.invertTree(root.left)
            r = self.invertTree(root.right)
            root.left = r
            root.right = l
            return root
        else:
            return None
