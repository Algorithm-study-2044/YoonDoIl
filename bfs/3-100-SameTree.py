class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            m = p.val == q.val
            return l and r and m
        elif not p and not q:
            return True
        else:
            return False
